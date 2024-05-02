import socket
import threading

HOST = "localhost"
PORT = 5050

def send(client: socket.socket, name: str):
    while True:
        message = input(f"{name}: ")
        client.send(message.encode())

def receive(client: socket.socket):
    while True:
        message = client.recv(64).decode()
        print(message)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    name = input("Enter a nickname: ")
    client.send(name.encode())
    
    send_thread = threading.Thread(target=send, args=(client, name))
    send_thread.start()
    
    receive_thread = threading.Thread(target=receive, args=(client,))
    receive_thread.start()
    
    

if __name__ == "__main__":
    main()