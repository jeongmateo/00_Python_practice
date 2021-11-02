import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) #soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs)   #a element 의 속성 정보를 출력
#
# print(soup.a["href"])   #a element 의 속성값 정보를 출력

# page에 대한 이해도가 낮을 때
# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# print(soup.find(attrs={"class":"Nbtn_upload"}))

#print(soup.find("li",attrs={"class":"rank01"}))

# rank1 = soup.find("li",attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

rankList = []
rank = soup.find("li",attrs={"class":"rank01"})

for i in range(1,10):
    rankList.append(rank.a.get_text())
    rank = rank.next_sibling.next_sibling
rankList.append(rank.a.get_text())

# for i in len(rankList):
    # print(rankList[i])
print(rankList)

# print(rank1.parent.a.get_text())
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

# webtoon = soup.find("a",text="2021 최애캐 안녕, 잘 지내니?-4화. <검은인간> 깜장이의 소원성취")
# print(webtoon)