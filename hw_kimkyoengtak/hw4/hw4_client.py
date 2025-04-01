import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9001)
sock.connect(addr)

while True:
    msg = input('Please enter the calculation function: ')

    # 서버측에서 q에 대해서 처리 해줌
    # if msg == 'q':
    #     break
    sock.send(msg.encode())
    response = sock.recv(1024).decode()
    print(response)

    if response == 'disconnect':
        break

sock.close()