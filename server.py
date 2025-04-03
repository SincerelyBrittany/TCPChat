import socket
import threading

# Server Configuration
HOST = '127.0.0.1'  # Localhost
PORT = 55556        # Port number

# Start Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
