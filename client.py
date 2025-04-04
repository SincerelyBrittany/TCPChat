import socket
import threading

# Get the user's nickname
user_nickname = input("Choose your nickname: ")

# Create and connect the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 55556))

# Function to receive messages from the server
def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode('ascii')
            if message == "NICK":
                client_socket.send(user_nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client_socket.close()
            break

# Function to send messages to the server
def send_message():
    while True:
        message = input(f"{user_nickname}: ")
        if message.lower() == 'exit':
            client_socket.send(f"{user_nickname} has left the chat.".encode('ascii'))
            client_socket.close()
            break
        else:
            full_message = f"{user_nickname}: {message}"
            client_socket.send(full_message.encode('ascii'))

# Start receiving and sending threads
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

write_thread = threading.Thread(target=send_message)
write_thread.start()
