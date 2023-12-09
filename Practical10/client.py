import socket
import json

# Create a UDP socket for the DNS client
dns_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# DNS server address and port
dns_server_address = ("127.0.0.1", 53)

# User input: Enter the hostname to resolve
hostname_to_resolve = input("Enter the hostname to resolve: ")

# Prepare the request in JSON format
dns_request = {"hostname": hostname_to_resolve}

# Send the request to the DNS server
dns_client_socket.sendto(json.dumps(dns_request).encode(), dns_server_address)

# Receive the response from the DNS server
data, dns_server_address = dns_client_socket.recvfrom(1024)

# Parse the JSON response
dns_response = json.loads(data.decode())

# Print the resolved IP address
print(f"Resolved IP address for {hostname_to_resolve}: {dns_response['ip_address']}")

# Close the socket
dns_client_socket.close()
