# TCPChat

# TCP Chat Application

This is a simple TCP-based chat application built using Python. It allows multiple clients to connect to a server and communicate in real time.

## Features
- Multiple clients can join the chat.
- Messages are broadcasted to all connected clients.
- Clients can join and leave the chat dynamically.
- Simple implementation using Python sockets and threading.

## Prerequisites
- **Python 3.10 or higher** (Check your version by running `python3 --version`)

## Installation
1. **Clone the Repository** 

## Usage

### 1. Run the Server
```sh
python3 server.py
```
You should see:
```
Server is running...
```

### 2. Run the Client
Open a new terminal and run:
```sh
python3 client.py
```
Enter a nickname when prompted.

### 3. Connect Multiple Clients
Open additional terminals and run more instances of `client.py` to simulate multiple users.

## Troubleshooting
- **If the server does not start**, try a different port in `server.py` and `client.py` (e.g., `PORT = 5050`).
- **If messages are not showing up**, check if the server is running properly:
  ```sh
  lsof -i :55556
  ```
  If no process is listening, restart `server.py`.
- **Firewall Issues on macOS**: Allow Python through the firewall using:
  ```sh
  sudo /usr/libexec/ApplicationFirewall/socketfilterfw --unblockapp /usr/bin/python3
  ```

## Next Steps
- Add a GUI using Tkinter.
- Implement message encryption for security.
- Deploy on a remote server for real-world use.

---
Enjoy chatting! 🚀