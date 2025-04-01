import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9000))
sock.listen(2)

while True:
    client, addr = sock.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())

    student_name = client.recv(1024).decode()
    print(student_name)
    if student_name == 'kim kyeongtak':
        client.send((20201518).to_bytes(4, 'big'))
    else:
        client.send(b'wrong student_name request')

    client.close()