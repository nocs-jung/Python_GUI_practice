from tkinter import *

root = Tk()
root.title("GUI tests")
root.geometry("540x380+200+100")
root.resizable(False,False)

label1 = Label(root, text="버거를 선택하세요") 
burger_var=IntVar()
btn_Burger1 = Radiobutton(root, text="치즈버거", value=1, variable=burger_var)
btn_Burger2 = Radiobutton(root, text="불고기버거", value=2, variable=burger_var)
btn_Burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)
btn_Burger4 = Radiobutton(root, text="빅맥버거", value=4, variable=burger_var)
btn_Burger1.select()

label2 = Label(root, text="음료를 선택하세요") 
drink_var=StringVar()
btn_Drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_Drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_Drink3 = Radiobutton(root, text="커피", value="커피", variable=drink_var)
btn_Drink4 = Radiobutton(root, text="녹차", value="녹차", variable=drink_var)
btn_Drink1.select()

#선택한 값 가져오기
def btncmd():
    print(burger_var.get()) #버거 중 선택된 값을 출력
    print(drink_var.get())  #음료 중 선택된 값을 출력

btn = Button(root, text="주문하기", command=btncmd)

label1.pack()
btn_Burger1.pack()
btn_Burger2.pack()
btn_Burger3.pack()
btn_Burger4.pack()
label2.pack()
btn_Drink1.pack()
btn_Drink2.pack()
btn_Drink3.pack()
btn_Drink4.pack()
btn.pack()

root.mainloop()