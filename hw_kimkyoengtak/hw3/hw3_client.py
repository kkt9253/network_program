import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

sock.send(b'kim kyeongtak')
server_response = sock.recv(1024)
school_num  = int.from_bytes(server_response, 'big')
print(school_num)

sock.close()