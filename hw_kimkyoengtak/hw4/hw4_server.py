import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9001))
sock.listen(4)
print('waiting...')

while True:
    client, addr = sock.accept()
    print('connection from ', addr)

    while True:
        request = client.recv(1024).decode().replace(' ', '')

        if not request:
            break
        if request == 'q':
            client.send(b'disconnect')
            break
        
        operators = ['+', '-', '*', '/']
        value = 0

        for oper in operators:
            if (oper_idx := request.find(oper)) != -1:
                a = int(request[:oper_idx])
                b = int(request[oper_idx + 1:])
                if oper == '+':
                    value = a + b
                elif oper == '-':
                    value = a - b
                elif oper == '*':
                    value = a * b
                elif oper == '/':
                    value = round(a / b, 1)

                break
        
        client.send(str(value).encode())
        print(value)
    client.close()