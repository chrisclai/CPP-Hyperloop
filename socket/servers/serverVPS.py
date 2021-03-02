import sys
import socket
import time

from _thread import *
import threading  

# thread function 
def handle_client(conn, addr, ser): 
    #print(f"[NEW CONNECTION] {addr} connected.")
    
    while True:
        msg = conn.recv(16).decode('utf-8')
        print(msg)
        ser.write(msg.encode('utf-8'))

def Main(): 
    if len(sys.argv) != 1:
        print("Usage: python3 clientThread.py")
        sys.exit(1)

    host = "45.56.91.192"

    print(f"host found on ip: {host}")

    # set port number
    port = 1234
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 

    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 

    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    # a forever loop until client wants to exit 
    while True:  
        try:
            print(clientsocket.recv(4096).decode('utf-8'))
        except:
            print("Socket Closed.")
            s.close()
            break
    print("Program Terminated.") 

if __name__ == '__main__': 
    Main() 
