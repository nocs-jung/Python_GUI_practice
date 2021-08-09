from tkinter import *

root = Tk()
root.title("GUI tests")
root.geometry("540x380+540+300")
root.resizable(False,False)

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")  #right side에 위치, y축을 기준으로 위아래 움직임

#set이 없으면 스크롤을 내려도 다시 올라옴
#yscrollcommand=scrollbar.set 옵션으로 조절
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1,32):
    listbox.insert(END, str(i)+"일")
listbox.pack(side="left")

#listbox에서 상하로 움직이는 뷰를 처리해주는 부분
scrollbar.config(command=listbox.yview)

root.mainloop()