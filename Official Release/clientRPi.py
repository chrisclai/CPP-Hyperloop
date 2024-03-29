import sys
import serial
import time
import socket

from _thread import *
import threading

DATA_AMOUNT = 36

global templist
templist = [0, 0, 0, 0, 0]

global controllist
controllist = [0, 0]

global mainlist
mainlist = []
for i in range(0, DATA_AMOUNT):
    mainlist.append(i)

def control(connIn, connOut, addr): 
    print(f"[CONTROL] {addr} Successfully connected to control thread!")
    global controllist
    while True:
        try:
            msg = connIn.recv(16).decode('utf-8')
            print(msg)
            if not msg:
                pass
            else:
                if msg == "brakeoff":
                    connOut.write('b'.encode('utf-8'))
                    controllist[0] = 0
                    pass
                elif msg == "brakeon":
                    connOut.write('a'.encode('utf-8'))
                    controllist[0] = 1
                    pass
                elif msg == "motoroff":
                    connOut.write('z'.encode('utf-8'))
                    controllist[1] = 0
                    pass
                elif msg == "motoron":
                    connOut.write('y'.encode('utf-8'))
                    controllist[1] = 1
                    pass
                connOut.flush()
        except: 
            print("Could not send command into arduino!!!")
        # connIn = server ; connOut = arduino - doesn't have addr; it is serial 
        # addr is from server

def maindata(connIn, connOut, addr): 
    print(f"[MAIN] {addr} Successfully connected to main thread!")
    global templist
    global controllist
    global mainlist
    time.sleep(1)
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
        for x in range(0, DATA_AMOUNT):
            try:
                mainlist[x] = data[x]
            except Exception as e:
                print(f"Data structure not found. Reason: {e}. Trying again...")
        
def tempdata(connIn, connOut, addr): 
    print(f"[TEMP] {addr} Successfully connected to tempdata thread!")
    global templist
    while True:
        tempdataUNO = connIn.readline().decode('utf-8').split()
        for x in range(0, 5):
            templist[x] = tempdataUNO[x]

def senddata(connOut, addr): 
    print(f"[DATA] {addr} Successfully connected to main data stream thread!")
    global mainlist
    time.sleep(5)
    while True:
        # create string again with all of the list elements and send them out to the GUI
        dataSend = ""
        for x in mainlist:
            dataSend += str(x)  + " "
        print(dataSend)
        connOut.send(bytes(dataSend, 'utf-8'))
        time.sleep(0.1)

def Main():
    if len(sys.argv) != 2:
        print("Usage: python3 clientThread.py")
        sys.exit(1)
    
    serverIP = sys.argv[1]

    serNanoIMU = serial.Serial("/dev/ttyUSB0", 115200) # IMU Fast Data located here 
    serNanoTemp = serial.Serial("/dev/ttyUSB1", 115200) # Temp and Slow Data located here
    serNanoRF = serial.Serial("/dev/ttyUSB2", 115200) # RF and Control located here

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverIP, 1234))

    print(f"Connection from {serverIP} has been established!")

    # [THREAD] Control Thread to recieve inputs from the GUI, sends RF and control data over to the RF Nano
    thread_RFC = threading.Thread(target = control, args=(s, serNanoRF, serverIP))
    thread_RFC.start()
    
    # [THREAD] Recieves IMU data from the Nano, organizes data from other threads, and sends it off to the GUI
    thread_IMU = threading.Thread(target = maindata, args=(serNanoIMU, serNanoIMU, serverIP))
    thread_IMU.start()

    # [THREAD] Off-Sync thread to recieve temperature data from Nano
    thread_Temp = threading.Thread(target = tempdata, args=(serNanoTemp, s, serverIP))
    thread_Temp.start()

    # [THREAD] Thread to send data to GUI (prevents arduino from getting stuck)
    thread_data = threading.Thread(target = senddata, args=(s, serverIP))
    thread_data.start()

    # [THREAD] Thread to calculate ping
    # thread_ping = threading.Thread(target = senddata, args=(serverIP))
    # thread_ping.start()
    
if __name__ == '__main__': 
    Main() 
