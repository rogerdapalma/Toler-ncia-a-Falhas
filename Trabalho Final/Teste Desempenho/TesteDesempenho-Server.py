import socket
import time

def start_server(host='localhost', port=12345, num_clients=2):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(num_clients)
    print(f"Server listening on {host}:{port}")

    clients = []
    message_history = []  # Buffer de histórico para armazenar mensagens enviadas
    retransmission_count = 0

    while len(clients) < num_clients:
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")
        clients.append(client_socket)

    # Enviar uma mensagem para todos os clientes e armazenar no histórico
    message = b"Hello, this is a reliable broadcast test message."
    message_history.append(message)
    
    start_time = time.time()
    
    for client_socket in clients:
        client_socket.sendall(message)

    # Receber ACK ou NACK de cada cliente e retransmitir se necessário
    for client_socket in clients:
        response = client_socket.recv(1024)
        if response == b"NACK":
            print("NACK received, retransmitting message")
            retransmission_count += 1
            for msg in message_history:  # Retransmitir todas as mensagens do histórico
                client_socket.sendall(msg)
        else:
            print("ACK received")
    
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Fechar conexões
    for client_socket in clients:
        client_socket.close()
    server_socket.close()

    print(f"Total retransmissions: {retransmission_count}")
    print(f"Total time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    start_server()
