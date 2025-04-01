import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9005)
sock.connect(addr)

while True:
    msg = input('Please enter the calculation function: ')
    if msg == 'q': 
        break
    sock.send(msg.encode())
    response = sock.recv(1024).decode()
    print(response)

sock.close()