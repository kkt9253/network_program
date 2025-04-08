from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    
    req_lines = c.recv(1024).decode().split('\r\n')
    startLine = req_lines[0]
    tokens = startLine.split()
    
    if tokens[0] == 'GET' and tokens[2] == 'HTTP/1.1':
        fileName = tokens[1][1:]
        
        header = ''
        body = ''
        if fileName.endswith('.html'):
            f = open(fileName, 'r', encoding='utf-8')
            body = f.read().encode('euc-kr')
            mimeType = 'text/html'
                
        elif fileName.endswith('.png'):
            f = open(fileName, 'rb')
            body = f.read()
            mimeType = 'image/png'
            
        elif fileName == 'favicon.ico':
            f = open(fileName, 'rb')
            body = f.read()
            mimeType = 'image/x-icon'
            
        else:
            c.send(b'HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>')
            continue
            
        header = 'HTTP/1.1 200 OK\r\n' \
            'Content-Type: ' + mimeType + '\r\n' \
                '\r\n'   
        c.send(header.encode())
        c.send(body)
        
    else:
        continue
    
    c.close()