import sys
import socket
import serial 
import time

from _thread import *
import threading 

print_lock = threading.Lock() 

# thread function 
def handle_client(conn, addr): 
    print(f"[NEW CONNECTION] {addr} connected.")
    
    while True:
        msg = conn.recv(16).decode('utf-8')
        print(msg)

def Main(): 
    if len(sys.argv) != 1:
        print("Usage: python3 clientThread.py")
        sys.exit(1)

    host = socket.gethostbyname(socket.gethostname())

    # read serial data from the arduino
    ser = serial.Serial("/dev/ttyACM0", 9600)

    # quick reset serial data
    time.sleep(1)
    data = ser.readline()
    time.sleep(1)
    data = 0

    # set port number
    port = 1234
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 

    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 

    # a forever loop until client wants to exit 
    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!")
        while True:
            thread = threading.Thread(target = handle_client, args=(clientsocket, address))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

            data = ser.readline()
            decoded = data.decode('utf-8').strip()
            print(decoded)
            clientsocket.send(bytes(decoded, 'utf-8'))
            time.sleep(0.1)
    s.close() 


if __name__ == '__main__': 
    Main() 
