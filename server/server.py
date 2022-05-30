import socket


sock = socket.socket()
sock.bind(('', 9090))
hostname = socket.gethostname()
ip = socket.gethostbyname_ex(hostname)
print(ip)

sock.listen(1)
while True:
    conn, addr = sock.accept()
    print(conn, addr)
