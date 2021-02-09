import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.68.123", 1234))

message = s.recv(1024)
print(message.decode('utf-8'))