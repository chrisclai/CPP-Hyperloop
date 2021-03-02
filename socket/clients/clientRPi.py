import sys
import serial
import time
import socket

def Main():
    if len(sys.argv) != 2:
        print("Usage: python3 clientThread.py")
        sys.exit(1)
    
    serverIP = sys.argv[1]

    ser = serial.Serial("/dev/ttyACM0", 115200)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverIP, 1234))

    print(f"Connection from {serverIP} has been established!")
    while True:
        data = ser.readline()
        try:
                decoded = data.decode('utf-8')
                print(decoded)
                s.send(bytes(decoded, 'utf-8'))
                time.sleep(0.1)
        except UnicodeDecodeError:
                print("unicode error detected... anyways,")

if __name__ == '__main__': 
    Main() 
