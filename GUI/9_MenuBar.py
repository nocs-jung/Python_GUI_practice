from tkinter import *

root = Tk()
root.title("GUI tests")
root.geometry("540x380+200+100")
root.resizable(False,False)

#기본틀에 메뉴 선언
menu = Menu(root)

#File 메뉴 생성
menu_file=Menu(menu,tearoff=0)
menu_file.add_command(label="New File")
menu_file.add_command(label="New Window")
menu_file.add_separator()           #서브 메뉴 리스트를 구분해 주는 선
menu_file.add_command(label="Open File")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)      #File메뉴에 포함된 모든 서브 메뉴를 연결

menu.add_cascade(label="Edit")

#view 메뉴 추가(check 버튼을 통해서 택1)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu_view.add_checkbutton(label="Show Maxmap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)

root.mainloop()