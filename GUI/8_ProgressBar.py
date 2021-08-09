from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("GUI tests")
root.geometry("540x380+200+100")
root.resizable(False,False)

progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
#mode option
#indeterminate: 결정되지 않고 언제 끝날지 모를 경우 좌우로 움직임
#determinate: 좌측부터 우측으로 채워짐
progressbar.pack()

#프로그레스 바 제어하기
#작동/정지
progressbar.start(10)   #10ms로 움직임, 작을수록 빠르게 움직임
#progressbar.stop()      #정지시킬 때

#전송 버튼 이용, 프로그레스 바 만들기
p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd():
    for i in range(1, 101):     #0~100, 1씩 채워지는 프로그레스 바
        time.sleep(0.01)        #0.01초 대기, 조금씩 타임딜레이

        p_var2.set(i)           #progressbar2의 값 설정 1-100까지 한번에 가지 않음
        progressbar2.update()   #ui 업데이트

        print(p_var2.get())     #직접 표현

btn = Button(root, text="전송", command=btncmd)
btn.pack()

root.mainloop()