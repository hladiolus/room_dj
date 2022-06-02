import socket
from pynput.keyboard import Key, Controller


sock = socket.socket()

host = input('enter host: ')

while True:
    try:
        port = input('enter port: ')
        port = int(port)
        break
    except:
        print('wrong port try again')


conn = sock.connect((host, port))
