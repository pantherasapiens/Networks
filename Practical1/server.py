import socket
import datetime
import signal
import sys

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

def signal_handler(sig, frame):
    print('Server shutting down...')
    server_socket.close()
    sys.exit(0)

# Set up a signal handler for Ctrl + C
signal.signal(signal.SIGINT, signal_handler)

while True:
    try:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Get the current date and time
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = f"Server time: {current_time}"

        # Send the response back to the client
        client_socket.sendall(response.encode('utf-8'))

        # Close the connection
        client_socket.close()

    except KeyboardInterrupt:
        # Handle Ctrl + C to gracefully shut down the server
        print('Server received KeyboardInterrupt. Shutting down...')
        server_socket.close()
        sys.exit(0)
