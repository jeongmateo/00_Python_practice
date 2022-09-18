from multiprocessing.sharedctypes import Value
from tkinter import *
from turtle import left
import tkinter.ttk as ttk

root = Tk()
root.title("Naming Rule Generator")     # 프로그램 이름
root.geometry("900x600")    # 창 가로 X 세로 크기 
# root.resizable(False, False)  # X(너비),Y(높이) 변경 불가 (창 크기 변경 불가)

# First label for selecting type(GIT or PTC)
Label(root, text="1. GIT or PTC Type을 고르세요.").place(x=10,y=30)

# Radio buttin of GIT/PTC
btn_Select = IntVar()  # 여기에 int 형으로 값을 저장한다.
btn_PTC = Radiobutton(root, text="PTC", value=1, variable=btn_Select)
btn_GIT = Radiobutton(root, text="GIT", value=2, variable=btn_Select)
btn_PTC.select()
btn_PTC.place(x=10, y=60)
btn_GIT.place(x=10, y=90)

frame_GIT = Frame(root, relief="solid", bd=1)
values_SWE = ["SWE1","SWE2","SWE3","SWE4","SWE5","SWE6"]   # SWE
lbl_SWE = Label(frame_GIT, text="2. SWE를 선택하세요.").pack(side="top")
btn1 = Button(frame_GIT, text="동작하는 버튼").pack(side="bottom")

readonly_combobox = ttk.Combobox(frame_GIT, values=values_SWE, state="readonly")  # 읽기 전용
readonly_combobox.current(0)
readonly_combobox.pack(side="left")




def btncmd():
    if btn_Select.get() == 1:
        print("PTC Selected")
        frame_GIT.grid(padx=10,pady=200)    
    elif btn_Select.get() == 2:
        print("GIT Selected")
        frame_GIT.grid_forget()
    
        
btn_sel1 = Button(root,text="GIT or PTC", command=btncmd)
btn_sel1.place(x=10,y=120)




root.mainloop()             # 해당 프로그램이 지속적으로 돌아가도록
