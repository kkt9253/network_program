from socket import *

s1 = socket(AF_INET, SOCK_STREAM)
s1.connect(('', 5001))
s2 = socket(AF_INET, SOCK_STREAM)
s2.connect(('', 5002))

while True:
    request = input('enter a device_id : ')
    
    response = ''
    if request == 'quit':
        s1.send(request.encode())
        s2.send(request.encode())
        break
    
    elif request == '1':
        s1.send(b'Request')
        response = s1.recv(1024).decode()
        
    elif request == '2':
        s2.send(b'Request')
        response = s2.recv(1024).decode()
        
    else:
        break
    
    with open('data.txt', 'a') as f:
        print(response)
        f.write(response + "\n")

s1.close()
s2.close()