from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create RPC server
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Function to add two numbers
    def add(x, y):
        return x + y

    # Function to subtract two numbers
    def subtract(x, y):
        return x - y

    # Register functions with the server
    server.register_function(add, 'add')
    server.register_function(subtract, 'subtract')

    print("RPC Server listening on port 8000...")
    server.serve_forever()
