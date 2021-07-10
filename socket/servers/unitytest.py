import socket
import json

from _thread import *
import threading

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8009        # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 8162 
TIME_OUT = 5
SENSOR_COUNT=1

def read_async(connIn, addr): 
    print(f"[NEW CONNECTION] {addr} connected to r-w-a thread.")
    while True:
        try:
            msg = connIn.recv(4096).decode('utf-8')
            print(msg)
            if msg == "hello":
                connIn.send(bytes("Why hello there!", "utf-8"))
            else:
                connIn.send(bytes("I don't understand this yet. Please try again later.", 'utf-8'))
        except:
            print(f"Packet recieve attempt to {addr} failed. Closing connection.")
            connIn.close()
            break

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT)) #Bind system socket
s.listen(SENSOR_COUNT) #Listen for up to SENSOR_COUNT connections
s.settimeout(TIME_OUT) 
print("Listening on %s:%s..." % (HOST, str(PORT)))

while True:
    try:
        conn, addr = s.accept()
        print(f"Connection from {addr} has been established!")
        # Begin data reading thread
        read_thread = threading.Thread(target = read_async, args = (conn, addr))
        read_thread.start()
    except:
        pass