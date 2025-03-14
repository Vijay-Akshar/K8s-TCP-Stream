import socket
import time

SERVER_HOST = "server-service"  # Use the Kubernetes service name
SERVER_PORT = 12345

def send_even_numbers():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        num = 2
        while True:
            message = str(num).encode()
            client_socket.sendall(message)
            print(f"Sent: {num}")
            num += 2
            
            # Send Keep-Alive every 10 seconds
            time.sleep(10)
            client_socket.sendall(b"KEEP_ALIVE")

if __name__ == "__main__":
    send_even_numbers()
