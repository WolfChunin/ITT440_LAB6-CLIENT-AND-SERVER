import socket

IP_ADDR = "192.168.46.9"
PORT_NUM = 8888

print('Welcome to the calculator! \n - Press X if you want to close the connection \n')
print(''' PLEASE INSERT THE NUMBER CATEGORY FOR EACH FUNCTION \n
 1 - Logarithmic Function \n 2 - Square Root Function \n 3 - Exponential Function \n 4 - Addition Function \n 5 - Suntraction Function \n 6 - Multiplication Function \n 7 - Division Function''')

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    print('Insert which function you want to execute')
    a = input()

    if a == '1':
        print('Insert the Value')
        b = input()
        print('Insert the Base Value')
        base = input()
        message = a +', '+b+', '+base

    elif a == '2':
        print('Insert the Value')
        c = input()
        message = a +', '+c

    elif a == '3':
        print('Insert the Exponent Value')
        exp = input()
        print('Insert the Base Value')
        base2 = input()
        message = a +', '+exp+', '+base2

    elif a == '4':
        print('Insert the First Value')
        b = input()
        print('Insert the Second Value')
        c = input()
        message = a +', '+b+', '+c

    elif a == '5':
        print('Insert the First Value')
        b = input()
        print('Insert the Second Value')
        c = input()
        message = a +', '+b+', '+c

    elif a == '6':
        print('Insert the First Value')
        b = input()
        print('Insert the Second Value')
        c = input()
        message = a+', '+b+', '+c
        
    elif a == '7':
        print('Insert the Numerator Value')
        num = input()
        print('Insert the Denominator Value')
        den = input()
        message = a+', '+num+', '+den

    else:
        break


    print('Message being send to server: ' + message + "\n")

    socket.sendto(message.encode('utf-8'), (IP_ADDR, PORT_NUM))
    if a == 'X' or a == 'x':
        break

    data, address = socket.recvfrom(2048)
    text = data.decode('utf-8')
    print('Result received from server %s : %s ' % (address, text) + "\n")

print('Connection Closed')
socket.close()
