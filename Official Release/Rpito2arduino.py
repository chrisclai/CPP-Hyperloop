import serial
import random
import time
if __name__ == '__main__':
    ser1 = serial.Serial("/dev/ttyUSB0", 115200) # reads serial from USB port 0
    ser2 = serial.Serial("/dev/ttyUSB1", 115200) # reads serial from USB port 1
    ser1.flush()
    ser2.flush()
    while True:
        time.sleep(1) # allows for a delay so it doesn't get clogged up and confused
        letter = ser1.readline().decode('utf-8').rstrip() # reads the serial that it got from the arduino transmitter and decodes it
        if letter == "x":
            print(letter)
            ser2.write(letter.encode('utf-8')) # sends out serial encoded in C++
        else:
            print(letter)
            ser2.write(letter.encode('utf-8')) # sends out serial encoded in C++
