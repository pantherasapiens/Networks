import socket
import threading

# Function to handle incoming client connections
def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    # Send a welcome message to the client
    client_socket.send("Welcome to the chat server!".encode())

    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break

        # Broadcast the received message to all connected clients
        broadcast_message = f"Client {client_address}: {data.decode()}"
        print(broadcast_message)
        broadcast(broadcast_message, client_socket)

    # Remove the client from the list when disconnected
    remove_client(client_socket)
    client_socket.close()

# Function to broadcast a message to all clients except the sender
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                # Remove the client from the list if unable to send
                remove_client(client)

# Function to remove a client from the list
def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
        print(f"Client {client_socket.getpeername()} disconnected")

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server.bind(("0.0.0.0", 5555))

# Listen for incoming connections
server.listen(5)
print("Server listening for connections...")

# List to store connected clients
clients = []

while True:
    # Accept a client connection
    client_socket, client_address = server.accept()

    # Add the client to the list
    clients.append(client_socket)

    # Create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
