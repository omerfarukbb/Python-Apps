import socket
import threading

HOST = "localhost"
PORT = 5050
clients = []

def handle_client(client: socket.socket, name: str):
    while True:
        message = client.recv(64).decode()
        print(f"{name}: {message}")
        for c in clients:
            c.send(f"{name}: {message}".encode())

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("The chat is started!")
    
    while True:
        client, _ = server.accept()
        name = client.recv(64).decode()
        print(f"{name} is joined to chat!")
        
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client, name))
        thread.start()

if __name__ == "__main__":
    main()