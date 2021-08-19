import socket
import threading
from queue import Queue
from typing import Counter

def Send(group, send_queue):
    print('Thread Send Start')
    while 1:
        try:
            #새롭게 추가된 클라이언트가 있을 경우 Send Thread를 새롭게 만들기 위해 루프를 빠져나감
            recv = send_queue.get()
            if recv == 'Group Changed':
                print('Group Changed')
                break
            
            #for문을 돌면서 모든 클라이언트에게 동일한 메시지를 보냄
            for conn in group:
                msg = 'Client'+str(recv[2])+'>> '+str(recv[0])
                if recv[1] != conn: #client 본인이 보낸 메시지는 받을 필요가 없기 떄문에 제외시킴
                    conn.send(bytes(msg.encode()))
                else:
                    pass
        except:
            pass

def Recv(conn, count, send_queue):
    print('Thread Recv '+str(count)+' Start')
    while 1:
        data = conn.recv(1024).decode()
        send_queue.put([data, conn, count]) #각각의 클라이언트의 메시지, 소켓정보, 쓰레드 번호를 send로 보냄

#TCP Echo Server
if __name__ == '__main__':
    send_queue = Queue()
    HOST = ""       #수신 받을 모든 IP를 의미
    PORT = 9000     #수신 받을 Port
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #TCP Socket
    server_sock.bind((HOST,PORT))                                       #소켓에 수신받을 IP주소와 Port를 설정
    server_sock.listen(10)                                              #소켓 연결, 여기서 파라미터는 접속수를 의미
    count = 0
    group = []      #연결된 클라이언트의 소켓정보를 리스트로 묶기 위함
    while 1:
        count += 1
        conn, addr = server_sock.accept()   #해당 소켓열고 대기
        group.append(conn)                  #연결된 클라이언트의 소켓정보
        print('Connected: '+str(addr))

        #소켓에 연결된 모든 클라이언트에게 동일한 메시지를 보내기 위한 쓰레드(브로드캐스트)
        #연결된 클라이언트가 1명 이상일 경우 변경된 group 리스트로 반영

        if count > 1:
            send_queue.put('Group Changed')
            thread1 = threading.Thread(target=Send, args=(group,send_queue,))
            thread1.start()
            pass
        else:
            thread1 = threading.Thread(target=Send,args=(group,send_queue,))
            thread1.start()

        #소켓에 연결된 각각의 클라이언트의 메시지를 받을 쓰레드
        thread2 = threading.Thread(target=Recv, args=(conn, count, send_queue,))
        thread2.start()

#Algorithm
#1. 9000번 포트를 열고 while 문을 무한으로 돌며 클라이언트를 기다림
#2. 클라이언트가 접속하면 count 를 1 증가시키고 group 이라는 리스트에 클라이언트 커넥션(conn) 정보를 담는다.
#3. 만약 접속자가 1명 이상일 경우 'Group Change'라는 메시지를 queue를 이용해 send쪽으로 보내 Send 쓰레드를 종료시키고 새로 접속한 사용가 포함된 group 리스트를 인자로하는 쓰레드를 재생성한다.
#4. Send 쓰레드가 생성되면 while 문을 돌며 Recv 쓰레드에서 queue를 통해 받은 메시지들 모든 클라이언트에게 보낸다. 
#   단, 클라이언트 자신이 보낸 메시지는 받을 필요가 없으므로 conn정보를 비교하여 자신에게는 보내지 않도록 한다.
#5. Recv쓰레드가 생성되면 while문을 돌며 메시지 받고 메시지를 보낸 상대의 conn정보와 메시지를 queue를 이용해 send로 보낸다.
#6. 이후  4번와 같은 작업을 반복한다.
