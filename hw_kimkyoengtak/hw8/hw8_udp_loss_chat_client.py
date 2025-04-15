from socket import *
import random

port = 3333
BUFF_SIZE = 1024

s = socket(AF_INET, SOCK_DGRAM)
s.connect(('', port))

while True:
    # 송신
    msg = input('-> ')
    cnt = 0
    while cnt <= 5:
        send_msg = f'[{cnt}] {msg}'
        s.send(send_msg.encode())
        s.settimeout(2)
        
        try:
            receive_ack = s.recv(BUFF_SIZE)
        except:
            cnt += 1
            continue
        else:
            if receive_ack != b'ack':
                cnt += 1
                continue
            break
    
    # 수신
    s.settimeout(None)
    while True:
        receive_msg = s.recv(BUFF_SIZE)
        if random.randint(1, 10) <= 5:
            continue
        s.send(b'ack')
        print(receive_msg.decode())
        break
    
        
        