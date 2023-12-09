import socket
import threading

# Function to handle receiving messages from the server
def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            break

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("127.0.0.1", 5555))

# Start a separate thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    # Get user input and send it to the server
    message = input()
    client_socket.send(message.encode())

# Close the client socket when done
client_socket.close()
