from tkinter import *

root = Tk()
root.title("LoganJ GUI")
root.geometry("640x480")  # 가로 X 세로

chkvar = IntVar()  # chkvar에 int형으로 값을 저장한다.
cheeckbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# cheeckbox.select()  # 자동 선택 처리
# cheeckbox.deselect()
cheeckbox.pack()

chkvar2 = IntVar()
checkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
checkbox2.pack()


def btncmd():
    print(chkvar.get())  # 0: 체크해제 / 1: 체크
    print(chkvar2.get())  # 0: 체크해제 / 1: 체크


btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()
