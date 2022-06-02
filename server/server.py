import socket

def getMyIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Создаем сокет (UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Настраиваем сокет на BROADCAST вещание.
    s.connect(('<broadcast>', 0))
    return s.getsockname()[0]

print(getMyIp())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9090))
hostname = socket.gethostname()
ip = socket.gethostbyname_ex(hostname)
print(ip)

sock.listen(1)
while True:
    conn, addr = sock.accept()
    print(conn, addr)
