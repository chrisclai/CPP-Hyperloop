txt = "hi there alex"

x = txt.split()


print (x[0])


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.86.38", 1234))

while(True):    
    message = s.recv(1024)
    num_array = message.decode('utf-8')
    # print (num_array.split())
    nums = num_array.split()
    print (nums[0])