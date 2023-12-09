import socket
import json

# DNS database mapping hostnames to IP addresses
dns_database = {
    "www.example.com": "192.168.1.1",
    "www.google.com": "8.8.8.8",
    "www.yahoo.com": "98.137.246.8",
}

# Create a UDP socket for the DNS server
dns_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
dns_server_socket.bind(("0.0.0.0", 53))
print("DNS Server listening for requests...")

while True:
    # Receive data and address from the DNS client
    data, dns_client_address = dns_server_socket.recvfrom(1024)
    print(f"Received DNS request from {dns_client_address}")

    try:
        # Parse the JSON request from the client
        dns_request = json.loads(data.decode())

        # Check if the requested hostname is in the DNS database
        if dns_request["hostname"] in dns_database:
            ip_address = dns_database[dns_request["hostname"]]
        else:
            ip_address = "Host not found in DNS database"

        # Prepare the response in JSON format
        dns_response = {"ip_address": ip_address}

        # Send the response back to the DNS client
        dns_server_socket.sendto(json.dumps(dns_response).encode(), dns_client_address)
    except json.JSONDecodeError:
        print("Error decoding JSON data from the DNS client")

# Close the socket (not reached in this example)
dns_server_socket.close()
