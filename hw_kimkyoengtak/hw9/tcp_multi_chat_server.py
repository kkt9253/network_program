from socket import *
import threading
import time

clients = []
thread_lock = threading.Lock()

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 2500))
s.listen(5)

print('tak server start!!!')

# quit 전까지 무한히 응답 작업 처리
def recvTask(client_sock, client_addr):
    while True:
        data = client_sock.recv(1024)
        
        # quit 받으면 clients에서 삭제 및 소켓 닫기
        # client로부터 [id]quit 형태로 전달 받기 때문에 in 사용
        # quit == data로 조건 잘못 지정해서 찾느라 하루종일...
        if b'quit' in data:
            print(client_addr, 'exited')
            with thread_lock:
                clients.remove(client_sock)
            client_sock.close()
            break
        
        print(time.asctime() + str(client_addr) + ':' + data.decode())
        
        # recv 대상이 아니라면 해당 채팅을 받아야하기에 send
        with thread_lock:
            for client in clients:
                if client != client_sock:
                    client.send(data)
    
while True:
    conn, addr = s.accept()
    # tcp니까 accept한 시점에 clients로 넣기 
    print('new client', addr)
    
    with thread_lock:
        clients.append(conn)
    
    # 이후 recv작업 thread에게 위임
    th = threading.Thread(target=recvTask, args=(conn, addr))
    th.start()