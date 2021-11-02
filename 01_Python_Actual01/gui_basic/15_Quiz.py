# Quiz) tkinter 를 이용한 메모장 프로그램 제작

#[GUI 조건]
# 1. title : 제목 없음 - Window 메모장 
# 2. 메뉴: 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리

from tkinter import *
import tkinter
import os
import tkinter.messagebox as msgbox

# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

filename = "mynote.txt"
def fileOpen():
    if os.path.isfile(filename):    #파일이 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf-8") as file:
            txt.delete("1.0",END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) #파일 내용을 본문에 입력

def fileSave():
    with open(filename, "w", encoding="utf-8") as file:
        file.write(txt.get("1.0",END))  #모든 내용을 가져와서 저장

root = Tk()
root.title("제목 없음")
root.geometry("640x480")

menu = Menu(root)


# menu 파일
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=fileOpen)
menu_file.add_command(label="저장", command=fileSave)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command= root.quit)

# 메모장이 root 전체에서 쓰고 있기 때문에 Scrollbar도
# 범위를 메모장이 아닌 Root로 놓고 사용하면 된다.

#스크롤바
scrollbar = Scrollbar(root)
txt = Text(root,yscrollcommand=scrollbar.set)
scrollbar.config(command=txt.yview)
scrollbar.pack(side="right",fill="y")
txt.pack(fill="both",expand=True)


# 기타 메뉴
menu_edit = Menu(menu, tearoff=0)
menu_text = Menu(menu, tearoff=0)
menu_view = Menu(menu, tearoff=0)
menu_help = Menu(menu, tearoff=0)

# 메뉴 추가
menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집", menu=menu_edit)
menu.add_cascade(label="서식", menu=menu_text)
menu.add_cascade(label="보기", menu=menu_view)
menu.add_cascade(label="도움말", menu=menu_help)

root.config(menu=menu)
root.mainloop()