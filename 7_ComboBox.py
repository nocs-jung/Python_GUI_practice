from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("GUI tests")
root.geometry("540x380+200+100")
root.resizable(False,False)

values = [str(i) + "일" for i in range(1,32)]   #1~31일, list type

#콤보박스에 값이 입력될 수 있음 ex."카드값 내기 싫어요"
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드결제일")      #최초 목록 제목 설정

#선택한 콤보 박스 내용 가져오기
def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="select", command=btncmd)
btn.pack()

#읽기전용(readonly) 콤보박스 만들기
readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0)        #실행 후 초기값으로 첫번째 목록을 선택
readonly_combobox.set("카드결제일2")
readonly_combobox.pack()

root.mainloop()