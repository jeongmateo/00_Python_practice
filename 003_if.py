# weather = input("오늘 날씨는 어떤가요?")

# if 조건:
#     실행 명령문

# if weather == "비" or "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("오늘은 맑습니다.")

temp = int(input("오늘의 기온은 어떤가요? "))

if 30 <= temp:
    print("너무 더워요 나가지 마세요")
elif 10 <= temp and temp <= 30:
    print("오늘은 날씨가 좋네요")
elif 0 <= temp <= 10:
    print("날씨가 쌀쌀하니 옷을 겉 옷을 챙기세요")
else:
    print("오늘은 날씨가 매우 추우니 나가지 마세요")
