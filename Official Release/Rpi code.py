import serial
import random
import time
if __name__ == '__main__':
    ser1 = serial.Serial("/dev/ttyUSB0", 115200)
    ser2 = serial.Serial("/dev/ttyUSB1", 115200)
    ser1.flush()
    ser2.flush()
    while True:
        time.sleep(1)
        letter = ser1.readline().decode('utf-8').rstrip()
        if letter == "x":
            print(letter)
            ser2.write(letter.encode('utf-8'))
        else:
            print(letter)
            ser2.write(letter.encode('utf-8'))