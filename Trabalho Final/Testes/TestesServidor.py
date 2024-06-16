import socket
import time

def start_server(host='localhost', port=12345, num_clients=2, timeout=5):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(num_clients)
    print(f"Server listening on {host}:{port}")

    clients = []
    message_history = []  # Buffer de histórico para armazenar mensagens enviadas
    retransmission_counts = {}

    while len(clients) < num_clients:
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")
        clients.append(client_socket)

    # Enviar uma mensagem para todos os clientes e armazenar no histórico
    message = b"Hello, this is a reliable broadcast test message."
    message_history.append(message)
    for client_socket in clients:
        client_socket.sendall(message)
        retransmission_counts[client_socket] = 0

    # Receber ACK ou NACK de cada cliente e retransmitir se necessário
    all_acks_received = False
    start_time = time.time()

    while not all_acks_received and time.time() - start_time < timeout:
        all_acks_received = True
        for client_socket in clients:
            client_socket.settimeout(timeout - (time.time() - start_time))
            try:
                response = client_socket.recv(1024)
                if response == b"NACK":
                    print("NACK received, retransmitting message")
                    for msg in message_history:
                        client_socket.sendall(msg)
                    retransmission_counts[client_socket] += 1
                    all_acks_received = False
                else:
                    print(f"ACK received from {client_socket.getpeername()}")
            except socket.timeout:
                print("Timeout reached, retransmitting message")
                for msg in message_history:
                    client_socket.sendall(msg)
                retransmission_counts[client_socket] += 1
                all_acks_received = False

    # Fechar conexões
    for client_socket in clients:
        client_socket.close()
    server_socket.close()
    print("Retransmission counts:", retransmission_counts)

if __name__ == "__main__":
    start_server()
