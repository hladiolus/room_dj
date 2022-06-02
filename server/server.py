import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostbyname(socket.gethostname())
sock.bind((IP, 9090))
hostname = socket.gethostname()
print(IP)


sock.listen(1)
while True:
    conn, addr = sock.accept()
    print(conn, addr)
