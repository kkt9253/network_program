# send [mboxID] message” 메시지 수신 시, 이미 존재하는 [mboxID]인지 확인
    # 존재 안한다면 딕셔너리에 [mboxID] 키로 만들고 값으로 list 할당한 후, message append
    # 존재한다면 그냥 message append
    
# receive [mboxID]” 메시지 수신 시, [mboxID] 키로 찾아 값의 list,pop(0)하고 해당 값 send(msg)

# quit 수신 시, 프로그램 종료

from socket import *

port = 9001
BUFF_SIZE = 1024
dict_ = {}

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('localhost', port))
print('client waiting...')

while True:
    req, addr = s.recvfrom(BUFF_SIZE)
    req_tokens = req.decode().split(' ', 2)
            
    if len(req_tokens) == 3 and req_tokens[0] == 'send':
        if not(req_tokens[1] in dict_.keys()):
            dict_[req_tokens[1]] = []
        dict_[req_tokens[1]].append(req_tokens[2])
        s.sendto(b'OK', addr)
        
    elif len(req_tokens) == 2 and req_tokens[0] == 'receive':
        if not(req_tokens[1] in dict_.keys()) or not(dict_[req_tokens[1]]):
            s.sendto(b'No messages', addr)
            continue
            
        msg = dict_[req_tokens[1]].pop(0)
        s.sendto(msg.encode(), addr)
        
    else:
        if len(req_tokens) != 1 or req_tokens[0] != 'quit':
            s.sendto(b'incorrect input... bye~', addr)
        break

s.close()