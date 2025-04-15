# 모든 수신, 송신 메시지는 화면에 표시 -> [] , <- []

# client에게 메시지 송신 시
    # ack 수신 못 받을 시, 타임아웃 2초, 최대 5번 재전송(재전송 횟수 표기)
    # ack 송신 시, 화면에   <- [idx] msg
    
# client에게 메시지 수신 시
# 50% 확률로 ack 안보냄 (데이터 손실 가정)
# ack 송신 시, 화면에    -> msg

from socket import *
import random

port = 3333
BUFF_SIZE = 1024

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', port))

while True:
    s.settimeout(None)
    
    # msg 수신
    while True:
        receive_msg, addr = s.recvfrom(BUFF_SIZE)
        if random.randint(1, 10) <= 5:
            continue
        s.sendto(b'ack', addr)
        print(f'<- {receive_msg.decode()}')
        break
        
    # msg 송신
    send_msg = input('-> ')
    cnt = 0
    while cnt <= 5:
        s.sendto(f'[{cnt}] {send_msg}'.encode(), addr)
        s.settimeout(2)
        
        try:
            receive_ack, addr = s.recvfrom(BUFF_SIZE)
        except:
            cnt += 1
            continue
        else:
            # 정해진 규약대로 안함, 본인은 규약대로 따르기 전까지 재전송하기로 선택
            if receive_ack != b'ack':
                cnt += 1
                continue
            break
        