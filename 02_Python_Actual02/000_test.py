import requests
from bs4 import BeautifulSoup

url = "https://form.office.naver.com/form/editor.cmd?docId=ZDVhNmExYmItMzNhNy00ZjVmLWJmMTQtYWYxYTIzOTVmZTA1&templateId=41002"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
print(res.status_code)

soup = BeautifulSoup(res.text, "lxml")

Naver = soup.find_all("a",{"class":"deleteOption column ui_button"})
print(Naver)