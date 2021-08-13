txt = "welcome to the jungle"

x = txt.split()

print(x)
print(x[0])
print(x[1])
print(x[2])
print(x[3])

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.19", 1234))

while(True):    
    message = s.recv(1024)
    numarray = message.decode('utf-8')
    #print(numarray.split())
    nums = numarray.split()
    #print(nums[0])
    print(int(nums[21])*2)
    
   