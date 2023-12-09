from xmlrpc.client import ServerProxy

# Create an RPC server proxy
server_proxy = ServerProxy('http://localhost:8000/RPC2')

# Call remote procedures
result_add = server_proxy.add(5, 3)
result_subtract = server_proxy.subtract(10, 4)

# Print results
print(f"Result of adding: {result_add}")
print(f"Result of subtracting: {result_subtract}")
