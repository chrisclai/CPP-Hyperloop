import sys
import socket
import time

def Main():
    if len(sys.argv) != 2:
        print("Usage: python3 clientThread.py <hostID>")
        sys.exit(1)

    serverIP = sys.argv[1]
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverIP, 1234))

    while(True):    
        message = s.send(bytes("hi", 'utf-8'))
        time.sleep(0.25)

if __name__ == '__main__': 
    Main() 