import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("GUI tests")
root.geometry("540x380+540+300")
root.resizable(False,False)

#1. 정보알림
def info():
    msgbox.showinfo(title="알림",message="정상적으로 예매 완료되었습니다")

#2. 경고
def warn():
    msgbox.showwarning(title="경고",message="해당 좌석은 매진되었습니다")

#3. 오류
def error():
    msgbox.showerror(title="에러",message="결제 오류가 발생했습니다")

#4. 요청/확인
def okcancel():
    msgbox.askokcancel(title="확인/취소",message="해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

#4. 재시도/취소
def retrycancel():
    msgbox.askretrycancel(title="재시도/취소",message="해일시적인 오류입니다/ 다시 시도하시겠습니까?")

#5. 예/아니오
def yesno():
    msgbox.askyesno(title="예/아니오",message="해당 좌석은 입구쪽입니다. 예매하시겠습니까?")

#6. 예/아니오/취소
def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매내역이 저장되지 않았습니다. \n 저장 후 다시 시작하시겠습니까?")
    
    if response == 1:   #예
        print("네")
    elif response ==0:  #아니오
        print("아니오")
    else:               #취소
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인/취소").pack()
Button(root, command=retrycancel, text="재시도/취소").pack()
Button(root, command=yesnocancel, text="예/아니오/취소").pack()

root.mainloop()