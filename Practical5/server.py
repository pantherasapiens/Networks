import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_socket.bind(("0.0.0.0", 5555))

print("Server listening for connections...")

while True:
    # Receive data and address from the client
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received from client at {client_address}: {data.decode()}")

    # Send a response back to the client
    response = "Hello, client! I received your message."
    server_socket.sendto(response.encode(), client_address)
