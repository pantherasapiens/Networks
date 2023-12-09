import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ("127.0.0.1", 5555)

# Send a message to the server
message = "Hello, server! How are you?"
client_socket.sendto(message.encode(), server_address)

# Receive the server's response and address
response, server_address = client_socket.recvfrom(1024)
print(f"Received from server at {server_address}: {response.decode()}")

# Close the socket
client_socket.close()
