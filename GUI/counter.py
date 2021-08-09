from tkinter import *

root = Tk()
root.title("KFE Counter")
#root.geometry("270x340+1100+100")
root.resizable(False,False)

menu = Menu(root)
menu_file=Menu(menu,tearoff=0)
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file) 
root.config(menu=menu)

number = 0
range = 1

def range_inc():
    global range
    range += 1
    range_lb.config(text=range)
def range_dec():
    global range
    range -= 1
    range_lb.config(text=range)
def number_inc():
    global number, range
    number += range
    number_lb.config(text=number)
def number_dec():
    global number, range
    number -= range
    number_lb.config(text=number)

number_lb = Label(root, bg="white", text=number, height=2)
range_lb = Label(root, text=range)

btn_number_inc = Button(root, text="증가", command=number_inc)
btn_number_dec = Button(root, text="감소", command=number_dec)
btn_range_inc = Button(root, text="▲", command=range_inc)
btn_range_dec = Button(root, text="▼", command=range_dec)

number_lb.grid(row=0, column=0, columnspan=3, sticky=N+E+W+S, padx=3, pady=3)
range_lb.grid(row=2, column=1, sticky=N+E+W+S)
btn_range_inc.grid(row=1, column=1, padx=3, pady=3, sticky=N+E+W+S)
btn_range_dec.grid(row=3, column=1, padx=3, pady=3, sticky=N+E+W+S)
btn_number_dec.grid(row=1, column=0, rowspan=3, padx=3, pady=3, sticky=N+E+W+S)
btn_number_inc.grid(row=1, column=2, rowspan=3, padx=3, pady=3, sticky=N+E+W+S)

root.mainloop()