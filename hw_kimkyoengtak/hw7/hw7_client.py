# 사용자한테 input 받아서 해당 문자열 서버로 전달
    # quit를 받는다면 서버에 전달 후 프로그램 종료
# 응답 받은 문자열 화면에 출력

from socket import *

port = 9001
BUFF_SIZE = 1024

s = socket(AF_INET, SOCK_DGRAM)
s.connect(('localhost', port))

while True:
    msg = input('Enter the message: ')
    
    s.send(msg.encode())
    if msg == 'quit':
        break
    
    res = s.recv(BUFF_SIZE).decode()
    print(res)
    
    if res == 'incorrect input... bye~':
        break
    
s.close()