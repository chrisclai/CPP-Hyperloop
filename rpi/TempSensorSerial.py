import serial
import RPi.GPIO as GPIO
import time
import tkinter as tk

ser = serial.Serial("/dev/ttyACM0", 9600)
ult = serial.Serial("/dev/ttyACM1", 9600)

root = tk.Tk()
root.title("TempSensorSerial")

disp = tk.StringVar()
disp.set("")

dispult = tk.StringVar()
dispult.set("")

message = ser.readline()
temp = ""

ultdata = ult.readline()
ultsonic = ""

def printTemp():
    message = ser.readline()
    temp = message.decode('utf-8')
    disp.set(temp)
    
    ultdata = ult.readline()
    ultsonic = ultdata.decode('utf-8')
    dispult.set(ultsonic)
    
    root.after(100, printTemp)

def lightson():
    ser.write(str.encode("led_on"))
    
def lightsoff():
    ser.write(str.encode("led_off"))
    
templabel = tk.Label(root, width=20, font=("Courier", 44), text="Current Temperature")
templabel.pack()

label = tk.Label(root, width=20, font=("Courier",44), textvariable=disp)
label.pack()

ultlabel = tk.Label(root, width=30, font=("Courier", 44), text="Ultrasonic Sensor Data Reading")
ultlabel.pack()

ultlabeldata = tk.Label(root, width=20, font=("Courier",44), textvariable=dispult)
ultlabeldata.pack()

button = tk.Button(root, width=20, font=("Courier",22), text="Turn LED On", command=lightson)
button.pack()

buttonoff = tk.Button(root, width=20, font=("Courier",22), text="Turn LED Off", command=lightsoff)
buttonoff.pack()

root.after(100, printTemp)
root.mainloop()