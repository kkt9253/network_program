from socket import *
import threading

server_addr = ('localhost', 2500)

# s 정의 앞에 안해놓으면 redvTask에서 읽을 때 문제생길까봐 앞에 둠
s = socket(AF_INET, SOCK_STREAM)
s.connect(server_addr)

def redvTask():
    while True:
        msg = s.recv(1024)
        print(msg.decode())

my_id = input('ID를 입력하세요: ')
s.send(('[' + my_id + ']').encode())

th = threading.Thread(target=redvTask)
# 부모랑 같이 종료되도록 설정
th.daemon = True
th.start()

while True:
    _input = input()
    msg = '[' + my_id + ']' + _input
    s.send(msg.encode())
    
    if _input == 'quit':
        break
    
s.close()