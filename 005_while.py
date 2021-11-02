# customer = ["아이언맨", "토르", "헐크"]
# index = 5

# while index >= 1:
#     print("{0}님, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer[0], index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다")

# while True:
#     print("{0}님, 커피가 준비 되었습니다. 호출 {1}회" .format(customer, index))
#     index += 1

customer = "한수"
person = "Unknown"

while person != customer:
    print("{0}님 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?  ")

print("즐거운 시간 되세요")
