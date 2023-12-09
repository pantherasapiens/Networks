import socket
import threading

# Create a TCP socket for the mail server
mail_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
mail_server_socket.bind(("0.0.0.0", 587))
print("Mail Server listening for connections...")

# List to store connected clients
mail_clients = []

def handle_mail_client(client_socket, client_address):
    print(f"Accepted mail connection from {client_address}")
    mail_clients.append(client_socket)

    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break

            # Process the received mail data (in a real server, this would involve handling email protocols)
            print(f"Received mail from {client_address}: {data.decode()}")
        except:
            break

    # Remove the client from the list when disconnected
    remove_mail_client(client_socket)
    client_socket.close()

def remove_mail_client(client_socket):
    if client_socket in mail_clients:
        mail_clients.remove(client_socket)
        print(f"Mail client {client_socket.getpeername()} disconnected")

# Listen for incoming connections
mail_server_socket.listen(5)

# Accept mail connections in a loop
while True:
    # Accept a mail client connection
    mail_client_socket, mail_client_address = mail_server_socket.accept()

    # Create a new thread to handle the mail client
    mail_client_thread = threading.Thread(target=handle_mail_client, args=(mail_client_socket, mail_client_address))
    mail_client_thread.start()
