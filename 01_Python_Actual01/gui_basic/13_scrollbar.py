import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Logan J")
root.geometry("640x480")    #가로 세로

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right",fill="y")

# set이 없으면 스크롤을 내려도 다시 올라온다
listbox = Listbox(frame, selectmode="extended", height=10,yscrollcommand= scrollbar.set)
for i in range(1,32): # 1~31 일
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

# 스크롤 바와 Listbox를 mapping 시켜준다.
scrollbar.config(command=listbox.yview)

root.mainloop()
