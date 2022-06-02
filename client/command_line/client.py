import socket

sock = socket.socket()

ip = input('Enter ip ')
port = input('Enter port ')
if port.isdigit():
    port = int(port)

sock.connect((ip, port))
