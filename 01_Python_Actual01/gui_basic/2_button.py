from tkinter import *

root = Tk()
root.title("LoganJ GUI")
root.geometry("640x480")  # 가로 X 세로
# root.geometry("640x480")  # 가로 X 세로 + x좌표 + y좌표

# root.resizable(False, False)  # X(너비),Y(높이) 변경 불가 (창 크기 변경 불가)

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")  # text의 수에 따라서 Button 의 크기 가변
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")  # 버튼의 크기가 고정
btn4.pack()

# For ground(fg) : 글자색   / Back ground(bg) : 배경색
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("버튼이 클릭 되었어요")


btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()
