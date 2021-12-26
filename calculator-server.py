import socket
import operator
import math
import sys
import time
import errno
from multiprocessing import Process


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("", 8888))

print('Server Listening At {}'.format(socket.getsockname()))

while True:
    messageBytes, address = socket.recvfrom(2048)
    messageString = messageBytes.decode('utf-8')
    print('Received from client {} : {}'.format(address, messageString))

    messageString = messageString.split(", ")
    a = messageString[0]

    if a == '1':
        b = messageString[1]
        base = messageString[2]
        result = (math.log(int(b),int(base)))

    elif a == '2':
        c = messageString[1]
        result = (math.sqrt(int(c)))

    elif a == '3':
        exp = messageString[1]
        base2 = messageString[2]
        result = (int(base2) ** int(exp))

    elif a == '4':
        b = messageString[1]
        c = messageString[2]
        result = float(b) + float(c)

    elif a == '5':
        b = messageString[1]
        c = messageString[2]
        result = float(b) - float(c)

    elif a == '6':
        b = messageString[1]
        c = messageString[2]
        result = float(b) * float(c)

    elif a == '7':
        num = messageString[1]
        den = messageString[2]
        result = float(num) / float(den)


    else:
        break
    
    if a == 'X' or a == 'x':
        break


    socket.sendto(str(result).encode(), address)


print('Connection Closed')
socket.close()

