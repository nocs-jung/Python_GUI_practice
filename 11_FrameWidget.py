from tkinter import *

root = Tk()
root.title("GUI tests")
root.geometry("540x380+540+300")
root.resizable(False,False)

Label(root, text="메뉴를 선택해주세요").pack(side="top")
Button(root, text="주문하기").pack(side="bottom")

#relief: 테두리모양
#bd: 외곽선 굵기
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="불고기버거").pack()
Button(frame_burger, text="치킨버거").pack()

#라벨 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()
Button(frame_drink, text="레모네이드").pack()

#프레임속성 지정하기
#side="left" / "right" : 프레임 위치 설정
#fill="both" : 지정한 위치에서 가득 채우고자 할 때
#expand=True : fill속성만 주면 한쪽으로 채움, expand속성을 True로 주면 전체적으로 퍼짐

root.mainloop()

