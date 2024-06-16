import socket
import random

def start_client(host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"Received: {message.decode()}")

            reply = input("Reply (type 'exit' to end): ")
            if reply.lower() == 'exit':
                break
            
            # Simulando falha no envio com 20% de probabilidade
            if random.random() < 0.2:
                print("Falha no envio")
                continue  # Não envia a resposta

            client_socket.sendall(reply.encode())
    except socket.error as e:
        print(f"Error: {str(e)}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
