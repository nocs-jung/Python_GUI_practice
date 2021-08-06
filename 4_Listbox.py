from tkinter import *

root = Tk()
root.title("GUI tests")
root.geometry("540x380+200+100")
root.resizable(False,False)

listbox = Listbox(root, selectmode="extended", height=0)
#selectmode = "extended" / "single"
#height=0, 리스트에 삽입된 목록 모두 보여달라
#height=3, 삽입된 목록 중 세 개만 화면에 나타남

#목록에 값을 넣어줄 때
listbox.insert(0, "대한민국")
listbox.insert(1, "독일")
listbox.insert(2, "미국")
#END는 몇 번째인지 신경 쓰지 않고 마지막에 목록을 넣을 때 사용
listbox.insert(END, "호주")
listbox.insert(END, "뉴질랜드")
listbox.pack()

#리스트/목록 삭제하기
def btncmd():
    #삭제
    #listbox.delete(END)     #클릭할 때마다 맨 뒤 항목 삭제
    listbox.delete(0)      #클릭할 때마다 맨 앞 항목 삭제
    
btn = Button(root, text="삭제", command=btncmd)
btn.pack()

#리스트 박스 속성
#size, get, curselection()
#listbox.size(): 목록 갯수 카운팅
#listbox.get(시작idx, 끝idx): 항목 가져오기
#listbox.curselection(): 선택된 항목 확인, tuple type으로 출력

root.mainloop()