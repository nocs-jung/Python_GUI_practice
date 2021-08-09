from tkinter import *

root = Tk()
root.title("GUI tests")
root.geometry("540x380+200+100")
root.resizable(False,False)

#텍스트 입력창 만들기
txt = Text(root, width=30, height=5)
txt.pack()

#텍스트 입력창에 글자 넣기
txt.insert(END, "글자를 입력하세요")

#엔트리 위젯 사용하기(한 줄짜리 텍스트 입력창)
ent = Entry(root, width=30)
ent.pack()
ent.insert(0, "한줄만 출력됩니다")

#버튼을 이용하여 텍스트와 엔트리 값 가져오는 방법
#get
def btnget():
    #첫 번째 라인부터 끝까지 가져와라
    #1.0:(첫번째 라인), 0(0번째 칼럼)   
    print(txt.get("1.0", END))
    #엔트리에 있는 내용 가져오라는 뜻
    print(ent.get())
btnget = Button(root, text="가져오기", command=btnget)
btnget.pack()

#버튼을 이용하여 텍스트와 엔트리 값 삭제하는 방법
#delete
def btndel():
    #첫번쨰 라인부터 끝까지 삭제해라
    txt.delete("1.0",END)
    #엔트리에 있는 내용을 지우라는 뜻
    ent.delete(0, END)

btndel = Button(root, text="지우기", command=btndel)
btndel.pack()

root.mainloop()