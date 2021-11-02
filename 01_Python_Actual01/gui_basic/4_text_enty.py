from tkinter import *

root = Tk()
root.title("LoganJ GUI")
root.geometry("640x480")  # 가로 X 세로

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")


e = Entry(root, width=30)       # 한줄로 입력 (로그인, ID /PW)받을 때
e.pack()
e.insert(0, "한 줄만 입력하세요.")


def btncmd():
    # Line 1부터 가져와라 / column 기준으로 0번째 부터 가져와라 (맨 왼쪽)
    print(txt.get("1.0", END))
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()
