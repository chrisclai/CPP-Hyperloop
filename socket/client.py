import socket
import tkinter as tk

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.68.123", 1234))

root = tk.Tk()
root.title("TempSensorSerial Output")

disp = tk.StringVar()
disp.set("")

message = s.recv(1024)
temp = ""

def printTemp():
    message = s.recv(1024)
    disp.set(message.decode('utf-8'))
    root.after(100, printTemp)

label = tk.Label(root, width=35, font=("Courier",44), textvariable=disp)
label.pack()

root.after(100, printTemp)
root.mainloop()