import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td",{"class":"title"})
scores = soup.find_all("div",{"class":"rating_type"})
total_rates = 0
for cartoon in range(0,len(cartoons)):
    title = cartoons[cartoon].a.get_text()
    link = ("https://comic.naver.com" + cartoons[cartoon].a['href'])
    score = "평점: " + (scores[cartoon].strong.get_text()).replace(" ","")
    total_rates += float(scores[cartoon].strong.get_text())
    print(title+"\t",link+"\t", score)
print("평균 평점:" , round(total_rates/len(cartoons),2))