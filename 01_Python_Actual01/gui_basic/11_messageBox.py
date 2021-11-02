import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Logan J")
root.geometry("640x480")    #가로 세로

#기차 예매 시스템
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")
def warn():
    msgbox.showwarning("경고", "예매에 실패하였습니다.")
def error():
    msgbox.showerror("에러", "날짜를 선택하지 않으셨습니다.")
def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매 하시겠습니까?")
def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적 오류입니다. 다시 시도하시겠습니까?")
def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매 하시겠습니까?")
def yesnocancel():
    response = msgbox.askyesnocancel(title=NONE, message="예매 내역이 저장되지 않았습니다. \n 저장 후 프로그램을 종료하시겠습니까?")
    if response == True:
        print("저장 후 종료")
    elif response == False:
        print("저장없이 종료")
    else:
        print("취소")
    #네: 저장 후 종료
    #아니오: 저장 하지 않고 종료
    #취소: 프로그램 종료 취소 

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()



root.mainloop()