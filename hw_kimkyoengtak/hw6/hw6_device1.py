from socket import *
import time, random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 5001))
s.listen(5)
print('Device 1 waiting connection...')

while True:
    c, addr = s.accept()
    print(f'connection client ip: {addr[0]}, port: {addr[1]}')
    
    while True:
        msg = c.recv(1024).decode()
    
        if msg == 'Request':
            response = time.ctime(time.time()) + ": "
            temp = random.randint(0, 40)
            humid = random.randint(0, 100)
            lilum = random.randint(70, 150)
            response += f"Device1: Temp={temp}, Humid={humid}, Iilum={lilum}"
            c.send(response.encode())
        
        else:
            c.close()
            break