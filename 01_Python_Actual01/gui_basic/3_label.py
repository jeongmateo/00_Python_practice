from tkinter import *

root = Tk()
root.title("LoganJ GUI")
root.geometry("640x480")  # 가로 X 세로

# label 은 글자 또는 이미지만 보여 준다.

photo = PhotoImage(file="gui_basic/img.png")
photo2 = PhotoImage(file="gui_basic/img2.png")

label1 = Label(root, text="안녕하세요")
label1.pack()

label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="또 만나요")
    # photo2 = PhotoImage(file="gui_basic/img2.png")    # 해당 위치에 두면 Garbage Collection 불필요한 메모리 공간 해제로 인해 해당 Image가 삭제 됨
    label2.config(image=photo2)


btn = Button(root, text="버튼1", command=change)
btn.pack()


root.mainloop()
