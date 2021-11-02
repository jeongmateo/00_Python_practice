from tkinter import *

root = Tk()
root.title("LoganJ GUI")
root.geometry("640x480")  # 가로 X 세로

Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar()  # 여기에 int 형으로 값을 저장한다.
btn_bugger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_bugger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_bugger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)
btn_bugger1.select()

btn_bugger1.pack()
btn_bugger2.pack()
btn_bugger3.pack()

Label(root, text="음료를 선택하세요").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink1.select()

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())  # 햄버거 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get())  # 햄버거 중 선택된 라디오 항목의 값(value)을 출력


btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()
