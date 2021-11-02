import requests
import tkinter.messagebox as msgbox

# 스마트폰 / 데스크탑 등... Browser가 접속할 때 header 정보에 따라서
# 보여지는 방식이 달라진다.
# 웹 크롤링 등을 할 때, 무단으로 막 가져다가 쓰면 부하가 심해질 수 있기 때문에 

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
res = requests.get(url,headers=headers)
# res.raise_for_status()      #웹 스크래핑 오류 시, 에러 발생 시킴


print(len(res.text))
print(res.text)

with open("nadocoding.html", "w",encoding="utf-8") as f:
    f.write(res.text)