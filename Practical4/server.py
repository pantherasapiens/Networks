import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(("0.0.0.0", 5555))

# Listen for incoming connections
server_socket.listen(5)
print("Server listening for connections...")

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive data from the client
    data = client_socket.recv(1024)
    print(f"Received from client: {data.decode()}")

    # Send a response back to the client
    response = "Hello, client! I received your message."
    client_socket.send(response.encode())

    # Close the connection with the client
    client_socket.close()
