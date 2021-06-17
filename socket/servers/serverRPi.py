import serial
import socket
import time

ser = serial.Serial("/dev/ttyACM0", 115200)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("192.168.68.120", 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    while True:
        data = ser.readline()
        try:
                decoded = data.decode('utf-8')
                print(decoded)
                clientsocket.send(bytes(decoded, 'utf-8'))
                time.sleep(0.1)
        except UnicodeDecodeError:
                print("unicode error detected... anyways,")
