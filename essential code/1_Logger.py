import logging

#logger 생성
logger = logging.getLoger("name")   #name에 아무것도 입력하지 않으면 root logger가 생성

#logger level 부여
logger.setLevel(logging.INFO)   #INFO레벨을 부여, INFO 이상의 메시지를 출력할 수 있다
                                #loger.info("message"), 소문자로 사용하면 메시지를 출력할 수 있다
                                #콘솔에만 출력, 정교하게 만들기위해서는 handler가 필요

#handler object는 log메시지의 level에 따라 적절한 log메시지를 지정된 위치에 전달하는 역할을 수행
#logger는 addHandler 메소드를 사용하여 handler를 추가함. 각각 다른 level과 format을 가질 수 있다

#StreamHandler와 FileHandler
#Stream(Console)에 메시지 전달, File에 메시지 전달

#formatter 설정
logging.Formatter(
  fmt = None,     # 메시지 출력 형태. None일 경우 raw 메시지를 출력.
  datefmt = None, # 날짜 출력 형태. None일 경우 '%Y-%m-%d %H:%M:%S'.
  style = '%'     # '%', '{', '$' 중 하나. `fmt`의 style을 결정.
)

# handler 객체 생성
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename="information.log")

# formatter 객체 생성
formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# handler에 level 설정
stream_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

# handler에 format 설정
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

#자식 logger는 부모 logger와 관련된 메세지를 전파(propagate)한다
#이러한 연결을 원하지 않는다면 logger의 propagate attribute를 False로 설정
logger.propagate = False

#logger에서 생성한 handler 추가하기
logger.addHandler(stream_handler)
logger.addHandler(file_handler)