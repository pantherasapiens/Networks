import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("127.0.0.1", 5555))

# Send a message to the server
message = "Hello, server! How are you?"
client_socket.send(message.encode())

# Receive the server's response
response = client_socket.recv(1024)
print(f"Received from server: {response.decode()}")

# Close the connection with the server
client_socket.close()
