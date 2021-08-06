from tkinter import *

root = Tk()
root.title("GUI tests")
root.geometry("540x380+200+100")
root.resizable(False,False)

#<<레이블 사용하기>>
label1 = Label(root, text="어서오세요")
label1.pack()

#레이블에 이미지 넣기
photo = PhotoImage(file=r"C:\Users\KFE\Pictures\setting.png")
label2 = Label(root, image=photo)
label2.pack()

#레이블 속성
def change():
    #1. 버튼 클릭시 텍스트 내용 변경하기
    label1.config(text="한국에 오신 것을 환영합니다")

    #2. 버튼 클릭시 이미지 변경하기
    global photo2       #프로그램 실행후 Garbage처리하지 않기 위해 필수!
    photo2 = PhotoImage(file=r"C:\Users\KFE\Pictures\wingsofliberty.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()