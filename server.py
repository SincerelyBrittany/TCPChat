import socket
import threading

# Server Configuration
SERVER_HOST = '127.0.0.1'  # Localhost
SERVER_PORT = 55556        # Port number

# Start Server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

active_clients = []
client_names = []


# Accept new clients and assign them a nickname
def accept_clients():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}")

        client_socket.send("NICK".encode('ascii'))
        client_name = client_socket.recv(1024).decode('ascii')

        client_names.append(client_name)
        active_clients.append(client_socket)

        print(f"Nickname: {client_name}")
        broadcast_message(f"{client_name} joined the chat!".encode('ascii'))
        client_socket.send("Connected to the chat!".encode('ascii'))

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

print("Server is running...")
accept_clients()
