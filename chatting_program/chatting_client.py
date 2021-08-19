import socket
import threading

def Send(client_sock):
    while 1:
        send_data = bytes(input().encode())     #사용자 입력
        client_sock.send(send_data)

def Recv(client_sock):
    while 1:
        recv_data = client_sock.recv(1024).decode()
        print(recv_data)

#TCP Client
if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #eTCP Socket
    HOST = 'localhost'  #통신할 대상의 IP주소
    PORT = 9000         #통신할 대상의 Port주소
    client_sock.connect((HOST,PORT))    #서버로 연결시도
    print('Connecting to ', HOST, ':', PORT)

    #Client의 메시지를 보낼 쓰레드
    thread1 = threading.Thread(target=Send, args=(client_sock,))
    thread1.start()

    #server로부터 다른 클라이언트의 메시지를 받을 쓰레드
    thread2 = threading.Thread(target=Recv, args=(client_sock,))
    thread2.start()

#Algorithm
#1. 소켓을 이용하여 9000번 포트 접속한다.
#2. Send 쓰레드와 Recv 쓰레드를 생성하여 동시에 메시지를 주고 받을 수 있도록 만들어준다.
#3. while 문을 돌며 input()함수를 이용하여 메시지를 작성하여 서버로 메시지를 보낸다.
#4. while 문을 돌며 서버로부터 메시지를 지속적으로 받아 출력한다.
