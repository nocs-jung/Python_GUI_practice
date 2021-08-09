from tkinter import *

root = Tk()
root.title("GUI tests")
root.geometry("540x380+200+100")
root.resizable(False,False)

chkclick = IntVar()     #chkclick에 int형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 그만 보기", variable=chkclick)

#기본으로 '체크'/'해제'하기
chkbox.select()     #체크박스 자동 선택
chkbox.deselect()   #체크박스 자동 해제

#체크 유무, 값으로 확인하기
#체크 해제: 0, 체크:1
def btncmd():
    print(chkclick.get())

btn = Button(root,text="체크 유무 확인", command=btncmd)

chkclick2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable=chkclick2)

chkbox.pack()
chkbox2.pack()
btn.pack()

root.mainloop()