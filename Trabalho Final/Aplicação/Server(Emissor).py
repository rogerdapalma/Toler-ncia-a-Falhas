
import socket
import random

def start_server(host='localhost', port=12345, num_clients=1):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(num_clients)
    print(f"Server listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    print(f"Connected to {addr}")
    
    try:
        while True:
            message = input("Enter message to send or type 'exit' to quit: ")
            if message.lower() == 'exit':
                break
            
            # Simulando falha no envio com 20% de probabilidade
            if random.random() < 0.2:
                print("Simulating sending failure")
                continue  # Não envia a mensagem

            client_socket.sendall(message.encode())

            response = client_socket.recv(1024)
            if not response:
                break
            print(f"Received: {response.decode()}")
    except socket.error as e:
        print(f"Connection error: {str(e)}")
    finally:
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    start_server()
