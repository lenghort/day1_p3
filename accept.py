import socket
HOST = '127.0.0.1'
PORT = 21001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"hi")
    data = s.recv(1024)
    print("Sever:", repr(data))