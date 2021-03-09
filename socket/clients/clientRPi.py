import sys
import serial
import time
import socket

from _thread import *
import threading

def read_write_async(connIn, connOut, addr): 
    print(f"[NEW CONNECTION] {addr} connected to r-w-a thread")
    while True:
        try:
            msg = connIn.recv(16)
            connOut.write(msg)
            print(msg.decode('utf-8'))
        except: 
            print(f"Packet write attempt to {addr} failed. Closing connection.")
            break
        # connIn = server ; connOut = arduino - doesn't have addr; it is serial 
        # addr is from server 

def Main():
    if len(sys.argv) != 2:
        print("Usage: python3 clientThread.py")
        sys.exit(1)
    
    serverIP = sys.argv[1]

    ser = serial.Serial("/dev/ttyACM0", 115200) # can write and read from it 
    # ser = serial.Serial("/dev/ttyACM1", 115200)
    nano = serial.Serial("/dev/ttyUSB0", 115200)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverIP, 1234))

    print(f"Connection from {serverIP} has been established!")
    thread_async = threading.Thread(target = read_write_async, args=(s, nano, serverIP))
    thread_async.start()
    # rasp pi wants to receive data asynchronously from server 
    
    time.sleep(3)
    
    while True:
        data = ser.readline() # how rasp pi receiving data from arduino \\ ser.writeline()
        # tempdata = tempard.readline()
        
        try:
                print(data.decode('utf-8'))
                # print(tempdata.decode('utf-8'))
                s.send(data) # send bytes over to socket (server)
        except UnicodeDecodeError:
                print("unicode error detected... anyways,")


if __name__ == '__main__': 
    Main() 
