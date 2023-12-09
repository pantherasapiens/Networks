import socket
import threading

# Create a TCP socket for the chat server
chat_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
chat_server_socket.bind(("0.0.0.0", 5555))

# Listen for incoming connections
chat_server_socket.listen(5)
print("Chat Server listening for connections...")

# List to store connected clients
chat_clients = []

def handle_chat_client(client_socket, client_address):
    print(f"Accepted chat connection from {client_address}")
    chat_clients.append(client_socket)

    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break

            # Broadcast the message to all connected clients
            broadcast_message = f"Client {client_address}: {data.decode()}"
            print(broadcast_message)
            broadcast(broadcast_message, client_socket)
        except:
            break

    # Remove the client from the list when disconnected
    remove_chat_client(client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    for client in chat_clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                remove_chat_client(client)

def remove_chat_client(client_socket):
    if client_socket in chat_clients:
        chat_clients.remove(client_socket)
        print(f"Chat client {client_socket.getpeername()} disconnected")

# Accept chat connections in a loop
while True:
    # Accept a chat client connection
    chat_client_socket, chat_client_address = chat_server_socket.accept()

    # Create a new thread to handle the chat client
    chat_client_thread = threading.Thread(target=handle_chat_client, args=(chat_client_socket, chat_client_address))
    chat_client_thread.start()
