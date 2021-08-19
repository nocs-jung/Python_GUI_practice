import socket
import threading
import logging
from queue import Queue

#logging setting
FORMAT = ('%(asctime)-15s %(threadName)-15s %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT, filename='Mk1.log', encoding='utf-8')
log = logging.getLogger()
log.setLevel(logging.ERROR)


_ASCII_HEADER = ">"
_ASCII_FOOTER = "\r\n"

def Send(conn, send_msg):
    log.info('Thread Send Start')
    print('Send city:'+bytes(send_msg.encode()))
    while True:
        try:
            recv = send_msg.get()
            msg = '해당 도시는'+str(recv[0])+'입니다'
            log.info('send msg:'+send_msg)
            conn.send(bytes(msg.encode()))
        except:
            pass


def Recv(conn, threads_cnt, send_msg):
    log.info('Thread Recv '+str(threads_cnt)+' Start')
    while True:
        data = conn.recv(1024).decode()
        print(data, type(data))
    
        if data == '02':
            city = '서울'
        elif data == '051':
            city = '부산'
        elif data == '053':
            city = '대구'
        elif data == '032':
            city = '인천'
        elif data == '062':
            city = '광주'
        elif data == '042':
            city = '대전'
        elif data == '052':
            city = '울산'
        elif data == '044':
            city = '세종'
        elif data == '031':
            city = '경기'
        elif data == '033':
            city = '강원'
        elif data == '043':
            city = '충북'
        elif data == '041':
            city = '충남'
        elif data == '063':
            city = '전북'
        elif data == '061':
            city = '전남'
        elif data == '054':
            city = '경북'
        elif data == '055':
            city = '경남'
        elif data == '064':
            city = '제주'
        else:
            city = '불명'
        print(city)
        send_msg.put([city, conn, threads_cnt]) #각각의 클라이언트의 메시지, 소켓정보, 쓰레드 번호를 send로 보냄


if __name__=="__main__":
    send_msg = Queue()
    HOST = ""       #received from all IP
    PORT = 9000     #received from 9000 port
    
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #TCP Socket
    server_sock.bind((HOST,PORT))                                       #소켓에 수신받을 IP주소와 Port를 설정
    server_sock.listen(10)                                              #소켓 연결, 여기서 파라미터는 접속수를 의미
    
    threads = []    #thread info array
    threads_cnt = 0

    while True:
        threads_cnt += 1
        conn, addr = server_sock.accept()   #해당 소켓열고 대기
        threads.append(conn)                #연결된 클라이언트의 소켓정보를 저장
        log.info('Connected: '+str(addr))

        if threads_cnt > 1:
            thread_send = threading.Thread(target=Send, args=(conn,send_msg, ))
            thread_send.start()

        thread_recv = threading.Thread(target=Recv, args=(conn, threads_cnt, send_msg,))
        thread_recv.start()