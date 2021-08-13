import sys
import socket
import time

from _thread import *
import threading  

# thread functions 
def read_write_async(connIn, connOut, addr): 
    print(f"[NEW CONNECTION] {addr} connected to r-w-a thread.")
    while True:
        try:
            msg = connIn.recv(16) # return address of utf 
            connOut.send(msg) # server will receive bytes from GUI and send to raspberry pi
            # print(msg.decode('utf-8'))
        except: 
            print(f"Packet receive attempt to {addr} failed. Closing connection.")
            connIn.close()
            break
    # server receives(read) 4096 bytes from GUI and send(write) over bytes to raspberry pi 
    # connIn = GUI and connOut = rasp 
    # address is from GUI 

def read_write_sync(connIn, connOut, addr):
    print(f"[NEW CONNECTION] {addr} connected to r-w-s thread.")
    while True:
        try:
            msg = connIn.recv(4096)
            # print(msg.decode('utf-8')) # test if data comes through
            connOut.send(msg) # server will receive bytes from raspberry pi and send to gui
        except:
            print(f"Packet send attempt to {addr} failed. Closing connection.")
            connOut.close()
            break
    # server gets information and sends information 
    # server receives(read) 4096 bytes from raspberry pi and send(write) over bytes to GUI 
    # raspberry pi sends 4096 to server 
    # gui receives 4096 bytes 

    # connIN = rasp and connOUT = GUI 
    # address is for GUI 

def Main(): 
    if len(sys.argv) != 1:
        print("Usage: python3 serverVPS.py <server IP>")
        sys.exit(1)

    host = sys.argv[1]

    print(f"host found on ip: {host}")

    # set port numbers
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
        time.sleep(3)

        while True:
            msg = rpiclientsocket.recv(4096)
            if not msg:
                rpiclientsocket.close()
                print("RPi disconnected. Closing socket.")
                print("Unable to continue process. Terminating script.")
                break
            else:
                # print(msg.decode('utf-8')) # test to see if data comes through
                pass
            try:
                conn, addr = s.accept()       
                print(f"Connection from {addr} has been established!")
                sockdict[conn] = addr
                print(f"Socket dictionary: {sockdict}")
                thread_sync = threading.Thread(target = read_write_sync, args=(rpiclientsocket, conn, addr))
                thread_sync.start()
                thread_async = threading.Thread(target = read_write_async, args=(conn, rpiclientsocket, addr))
                thread_async.start()
            except:
                pass   
    except:
        print("RPi not found. Please run program with connected device.")            

if __name__ == '__main__': 
    Main() 
