from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox as msgbox

root = Tk()
root.title("Calculator")
root.resizable(False,False)

formula = "0"
operator = 0
entered = 0

fontStyle = tkFont.Font(family="Lucida Grande", size=30)
display = Label(root, text=formula, bg="white", anchor="se", relief="solid", height=1, font=fontStyle)
display.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3, columnspan=4)

#숫자입력 함수
def btn0():
    global formula, entered
    if formula=="0" or entered == 1:
        formula = "0"
        entered = 0
    else:
        formula += "0"
    display.config(text=formula)
def btn1():
    global formula, entered
    if formula=="0" or entered == 1:
        formula = "1"
        entered = 0
    else:
        formula += "1"
    display.config(text=formula)
def btn2():
    global formula, entered
    if formula=="0" or entered == 1:
        formula = "2"
        entered = 0
    else:
        formula += "2"
    display.config(text=formula)
def btn3():
    global formula, entered
    if formula=="0" or entered == 1:
        formula = "3"
        entered = 0
    else:
        formula += "3"
    display.config(text=formula)
def btn4():
    global formula, entered
    if formula=="0" or entered == 1:
        formula = "4"
        entered = 0
    else:
        formula += "4"
    display.config(text=formula)
def btn5():
    global formula, entered
    if formula=="0" or entered == 1:
        formula = "5"
        entered = 0
    else:
        formula += "5"
    display.config(text=formula)
def btn6():
    global formula, entered
    if formula=="0" or entered == 1:
        formula = "6"
        entered = 0
    else:
        formula += "6"
    display.config(text=formula)
def btn7():
    global formula, entered
    if formula=="0" or entered == 1:
        formula = "7"
        entered = 0
    else:
        formula += "7"
    display.config(text=formula)
def btn8():
    global formula, entered
    if formula=="0" or entered == 1:
        formula = "8"
        entered = 0
    else:
        formula += "8"
    display.config(text=formula)
def btn9():
    global formula, entered
    if formula=="0" or entered == 1:
        formula = "9"
        entered = 0
    else:
        formula += "9"
    display.config(text=formula)

#기능 함수
def clear():
    global formula, operator
    formula = "0"
    operator = 0
    display.config(text=formula)
def delete():
    global formula
    if formula != "0":
        formula = formula[0:-1]
        if formula == "":
            formula = "0"
    display.config(text=formula)
def add():
    global formula, operator
    if operator == 0:
        formula += "+"
        operator = 1
        display.config(text=formula)
    else:
        msgbox.showwarning(title="경고",message="연산자는 하나만 사용할 수 있습니다")
def sub():
    global formula, operator
    if operator == 0:
        formula += "-"
        operator = 1
        display.config(text=formula)
    else:
        msgbox.showwarning(title="경고",message="연산자는 하나만 사용할 수 있습니다")
def mul():
    global formula, operator
    if operator == 0:
        formula += "×"
        operator = 1
        display.config(text=formula)
    else:
        msgbox.showwarning(title="경고",message="연산자는 하나만 사용할 수 있습니다")
def div():
    global formula, operator
    if operator == 0:
        formula += "÷"
        operator = 1
        display.config(text=formula)
    else:
        msgbox.showwarning(title="경고",message="연산자는 하나만 사용할 수 있습니다")
def point():
    global formula
    if formula.endswith("."):
        msgbox.showwarning(title="경고",message="소수점을 연속 입력할 수 없습니다")
    else:
        formula += "."
        display.config(text=formula)
def calc():
    global formula,entered, operator
    if formula.count('+') == 1:
        sliced_formula = formula.split('+')
        result = float(sliced_formula[0])+float(sliced_formula[1])
        display.config(text=str(result))
        entered = 1
        operator = 0
    elif formula.count('-') == 1:
        sliced_formula = formula.split('-')
        result = float(sliced_formula[0])-float(sliced_formula[1])
        display.config(text=str(result))
        entered = 1
        operator = 0
    elif formula.count('×') == 1:
        sliced_formula = formula.split('×')
        result = float(sliced_formula[0])*float(sliced_formula[1])
        display.config(text=str(result))
        entered = 1
        operator = 0
    elif formula.count('÷') == 1:
        sliced_formula = formula.split('÷')
        result = float(sliced_formula[0])/float(sliced_formula[1])
        display.config(text=str(result))
        entered = 1
        operator = 0
    else:
        msgbox.showwarning(title="경고",message="연산자를 입력해주세요")


#그리드를 이용한 키패드 만들기
#키패드 가장 윗줄 - function키 만들기
btn_F16 = Button(root, text="F1", width=7, height=2)
btn_F17 = Button(root, text="F2", width=7, height=2)
btn_F18 = Button(root, text="F3", width=7, height=2)
btn_F19 = Button(root, text="F4", width=7, height=2)

btn_F16.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_F17.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_F18.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_F19.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

#clear줄
btn_Clear = Button(root, text="Clear", width=7, height=2, command=clear)
btn_delete = Button(root, text="←", width=7, height=2, command=delete)
btn_Div = Button(root, text="/", width=7, height=2, command=div)
btn_Mul = Button(root, text="*", width=7, height=2, command=mul)

btn_Clear.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_delete.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_Div.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_Mul.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

#7줄
btn_7 = Button(root, text="7", width=7, height=2, command=btn7)
btn_8 = Button(root, text="8", width=7, height=2, command=btn8)
btn_9 = Button(root, text="9", width=7, height=2, command=btn9)
btn_sub = Button(root, text="-", width=7, height=2, command=sub)

btn_7.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

#4줄
btn_4 = Button(root, text="4", width=7, height=2, command=btn4)
btn_5 = Button(root, text="5", width=7, height=2, command=btn5)
btn_6 = Button(root, text="6", width=7, height=2, command=btn6)
btn_add = Button(root, text="+", width=7, height=2, command=add)

btn_4.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=4, column=3, sticky=N+E+W+S, padx=3, pady=3)

#1줄
btn_1 = Button(root, text="1", width=7, height=2, command=btn1)
btn_2 = Button(root, text="2", width=7, height=2, command=btn2)
btn_3 = Button(root, text="3", width=7, height=2, command=btn3)
btn_enter = Button(root, text="enter", width=7, height=2, command=calc)

btn_1.grid(row=5, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=5, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=5, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)

#0줄
btn_0 = Button(root, text="0", width=7, height=2, command=btn0)
btn_point = Button(root, text=".", width=7, height=2, command=point)

btn_0.grid(row=6, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn_point.grid(row=6, column=2, sticky=N+E+W+S, padx=3, pady=3)

#grid 속성 지정
#sticky=N+E+W+S : 동서남북 지정한 방향으로 버튼의 크기를 늘림
#padx, pady : 버튼 내 공간 띄우기, 그리드 내에 공간 띄우기
#width, height : 글자크기와 관계없이 크기 고정

root.mainloop()