import sys
import socket
import time

from _thread import *
import threading  

# thread function 
def read_write_async(connIn, connOut, addr): 
    print(f"[NEW CONNECTION] {addr} connected to r-w-a thread.")
    while True:
        msg = conn.recv(16).decode('utf-8')
        print(msg)
        connOut.send(bytes(msg, 'utf-8'))

def read_write_sync(connIn, connOut, addr):
    print(f"[NEW CONNECTION] {addr} connected to r-w-s thread.")
    while True:
        try:
            connOut.send(connIn.recv(4096))
        except:
            print(f"Packet send attempt to {addr} failed. Closing connection.")
            connOut.close()
            break

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
    s.settimeout(5) 
    print("socket is listening") 

    # dictionary of open sockets
    sockdict = {}

    try:
        # create a specialized socket just for the RPi on boot
        rpiclientsocket, rpiaddress = s.accept()
        sockdict[rpiclientsocket] = rpiaddress
        print(f"Connection from {rpiaddress} has been established! [THIS IS THE RASPBERRY PI]")

        while True:
            msg = connIn.recv(4096)
            if not msg:
                connIn.close()
                print("RPi disconnected. Closing socket.")
                print("Unable to continue process. Terminating script.")
                break
            try:
                conn, addr = s.accept()       
                print(f"Connection from {addr} has been established!")
                sockdict[conn] = addr
                print(f"Socket dictionary: {sockdict}")
                thread = threading.Thread(target = read_write_sync, args=(rpiclientsocket, conn, addr))
                thread.start()
            except:
                pass   
    except:
        print("RPi not found. Please run program with connected device.")            

if __name__ == '__main__': 
    Main() 
