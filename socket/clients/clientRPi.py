import sys
import serial
import time
import socket

from _thread import *
import threading

global templist
templist = [0, 0, 0, 0, 0]

global controllist
controllist = [0, 0]

def control(connIn, connOut, addr): 
    print(f"[CONTROL] {addr} Successfully connected to control thread!")
    global controllist
    while True:
        try:
            msg = connIn.recv(16).decode('utf-8')
            print(msg)
            connOut.write(msg.encode('utf-8'))
            if msg == "brakeoff":
                controllist[0] = 0
                pass
            elif msg == "brakeon":
                controllist[0] = 1
                pass
            elif msg == "motoroff":
                controllist[1] = 0
                pass
            elif msg == "motoron":
                controllist[1] = 1
                pass
        except: 
            print("Could not send command into arduino!!!")
        # connIn = server ; connOut = arduino - doesn't have addr; it is serial 
        # addr is from server

def maindata(connIn, connOut, addr): 
    print(f"[MAIN] {addr} Successfully connected to main thread!")
    global templist
    global controllist
    while True:
        # how rasp pi receiving data from arduino \\ ser.writeline()
        try:
            data = connIn.readline().decode('utf-8').split()
            # print(data)
        except UnicodeDecodeError:
            print("unicode error detected... anyways,")
        # update main data list with information from the temperature sensor readings and control readings
        for x in range(0, 5):
            try:
                data[x] = templist[x]
            except:
                pass
        try:
            data[34] = controllist[0]
            data[35] = controllist[1]
        except:
            print("Control list segment at fault. Trying again...")
        # create string again with all of the list elements and send them out to the GUI
        dataSend = ""
        for x in data:
            dataSend += str(x)  + " "
        print(dataSend)
        connOut.send(bytes(dataSend, 'utf-8'))
        
def tempdata(connIn, connOut, addr): 
    print(f"[TEMP] {addr} Successfully connected to tempdata thread!")
    global templist
    while True:
        tempdataUNO = connIn.readline().decode('utf-8').split()
        for x in range(0, 5):
            templist[x] = tempdataUNO[x]

def Main():
    if len(sys.argv) != 2:
        print("Usage: python3 clientThread.py")
        sys.exit(1)
    
    serverIP = sys.argv[1]

    serMega = serial.Serial("/dev/ttyACM0", 115200) # can write and read from it 
    serUno = serial.Serial("/dev/ttyACM1", 115200)
    serNano = serial.Serial("/dev/ttyUSB0", 115200)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverIP, 1234))

    print(f"Connection from {serverIP} has been established!")

    # [THREAD] Control Thread to recieve inputs from the GUI
    thread_async = threading.Thread(target = control, args=(s, serNano, serverIP))
    thread_async.start()
    
    # [THREAD] Recieves IMU data from the MEGA, organizes data from other threads, and sends it off to the GUI
    thread_main = threading.Thread(target = maindata, args=(serMega, s, serverIP))
    thread_main.start()

    # [THREAD] Off-Sync thread to recieve temperature data from UNO
    thread_temp = threading.Thread(target = tempdata, args=(serUno, s, serverIP))
    thread_temp.start()


if __name__ == '__main__': 
    Main() 
