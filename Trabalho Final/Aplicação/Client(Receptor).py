import socket
import random

def start_client(host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        message = client_socket.recv(1024)
        print(f"Received: {message.decode()}")

        # Simular a perda de mensagem com uma probabilidade de 20%
        if random.random() < 0.2:
            print("Simulating message loss")
            client_socket.sendall(b"NACK")
        else:
            print("Sending ACK")
            client_socket.sendall(b"ACK")
    except socket.error as e:
        print(f"Error receiving message: {e}")
        client_socket.sendall(b"NACK")

    client_socket.close()

if __name__ == "__main__":
    start_client()
