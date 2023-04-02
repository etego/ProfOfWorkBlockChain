import socket
import threading
import json

class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.peers = []

    def start(self):
        # Create a socket and bind it to the host and port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)

        print(f'Node started at {self.host}:{self.port}')

        while True:
            # Accept incoming connections
            connection, address = self.socket.accept()
            print(f'New connection from {address}')

            # Handle connection in a separate thread
            thread = threading.Thread(target=self.handle_connection, args=(connection, address))
            thread.start()

    def handle_connection(self, connection, address):
        data = connection.recv(1024)
        message = json.loads(data)

        if message['type'] == 'add_peer':
            self.peers.append((message['host'], message['port']))
            print(f'Added peer: {message["host"]}:{message["port"]}')
        elif message['type'] == 'get_peers':
            response = json.dumps({'type': 'peers', 'peers': self.peers})
            connection.send(response.encode())

        connection.close()

if __name__ == '__main__':
    node = Node('localhost', 5000)
    node.start()
