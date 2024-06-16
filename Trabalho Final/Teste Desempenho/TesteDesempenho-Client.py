import socket
import random
import time

def start_client(host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        start_time = time.time()
        message = client_socket.recv(1024)
        print(f"Received: {message.decode()}")

        # Simular a perda de mensagem com uma probabilidade de 20%
        if random.random() < 0.2:
            print("Simulating message loss")
            client_socket.sendall(b"NACK")
        else:
            print("Sending ACK")
            client_socket.sendall(b"ACK")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Total time for message processing: {elapsed_time:.2f} seconds")
    except socket.error as e:
        print(f"Error receiving message: {e}")
        client_socket.sendall(b"NACK")

    client_socket.close()

if __name__ == "__main__":
    start_client()
