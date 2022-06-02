import socket
import threading


class Client(object):
    def __init__(self, _socket, address):
        self.socket = _socket
        self.address = address


class Server:
    def __init__(self, host, port):
        self.clients = []
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        print(f'Started server at {self.host}:{self.port}')
        self.server_listener = threading.Thread(target=self.listen)

    def start(self):
        self.server_listener.start()
        print('started')

    def listen(self):
        self.sock.listen()
        print(self.sock)
        while True:
            client_socket, address = self.sock.accept()
            self.clients.append(Client(_socket=client_socket, address=address))
            print(address, 'connected')


if __name__ == '__main__':

    IP = socket.gethostbyname(socket.gethostname())
    PORT = 9090
    server = Server(IP, PORT)

    try:
        server.start()
    except Exception as error:
        print(error)
