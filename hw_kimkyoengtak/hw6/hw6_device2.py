from socket import *
import time, random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 5002))
s.listen(5)
print('Device 2 waiting connection...')

while True:
    c, addr = s.accept()
    print(f'connection client ip: {addr[0]}, port: {addr[1]}')
    
    while True:
        device_id = c.recv(1024).decode()
        
        if device_id == 'Request':
            response = time.ctime(time.time()) + ": "
            heartbeat = random.randint(40, 140)
            steps = random.randint(2000, 6000)
            cal = random.randint(1000, 4000)
            response += f"Device2: Heartbeat={heartbeat}, Steps={steps}, Cal={cal}"
            c.send(response.encode())
        
        else:
            c.close()
            break