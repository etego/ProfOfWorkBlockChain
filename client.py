import socket
import json

def send_message(host, port, message):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((host, port))
    connection.send(json.dumps(message).encode())

    data = connection.recv(1024)
    response = json.loads(data)
    connection.close()

    return response

# Example usage
# Add a new peer to the node at localhost:5000
send_message('localhost', 5000, {'type': 'add_peer', 'host': 'localhost', 'port': 5001})

# Get a list of peers from the node at localhost:5000
peers = send_message('localhost', 5000, {'type': 'get_peers'})
print(f'Peers: {peers["peers"]}')
