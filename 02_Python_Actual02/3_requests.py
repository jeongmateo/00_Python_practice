import requests
import tkinter.messagebox as msgbox

res = requests.get("http://google.com")
res.raise_for_status()      #웹 스크래핑 오류 시, 에러 발생 시킴
# res = requests.get("http://naver.com")
# print("응답코드 : ", res.status_code)   #200 이면 정상


# if res.status_code == requests.codes.ok:
#     msgbox.showinfo("알림", "통신이 정상적으로 동작합니다")
# else:
#     msgbox.showerror("경고","통신상에 문제가 생겼습니다. [에러코드 {} ]".format(res.status_code))


print(len(res.text))
print(res.text)

with open("mygoogle.html", "w",encoding="utf-8") as f:
    f.write(res.text)