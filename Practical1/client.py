import socket

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send a request to the server (you can send any data as the request)
client_socket.sendall(b"Request for date and time")

# Receive the response from the server
data = client_socket.recv(1024)
print(f"Received from server: {data.decode('utf-8')}")

# Close the connection
client_socket.close()
