from tkinter import *
from typing import Sized

#프레임 생성 및 설정
root = Tk()
root.title("GUI tests")                 #상단 타이틀 설정
root.geometry("540x380+200+100")        #대화창 크기 설정+표시될 좌표
root.resizable(False,False)             #프레임크기 조절을 허용하고 싶지 않을 때

#<<버튼 만들기>>
#속성
#text: 버튼에 표시될 메시지
btn1 = Button(root, text="버튼1")
btn1.pack()

#padx: 가로 padding
#pady: 세로 padding
btn2 = Button(root, text="버튼2", padx=10, pady=10)
btn2.pack()

#width: 너비
#height: 높이
btn3 = Button(root,text="버튼3", width=10, height=5)
btn3.pack()

#fg(foreground): 글자색
#bg(background): 배경색
btn4 = Button(root, text="버튼4", fg="green", bg="yellow")
btn4.pack()

#image: 이미지로 생성
#경로를 유니코드로 인식시 r''을 사용(unicodeescape error)
photo = PhotoImage(file=r"C:\Users\KFE\Pictures\setting.png")
btn5 = Button(root, image=photo)
btn5.pack()

#버튼을 동작 시키기
def btncmd():   #btncmd함수 설정
    print("버튼이 클릭되었습니다")
btn6 = Button(root,text="동작하는 버튼", command=btncmd)
btn6.pack()

root.mainloop()
