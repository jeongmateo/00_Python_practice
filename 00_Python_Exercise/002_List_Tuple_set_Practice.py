from random import *
users = range(1, 21)  # 1부터 20까지 숫자를 생성
# print(users,type(users))
users = list(users)
# print(users,type(users))

shuffle(users)
print(users)

winners = sample(users, 4)  # 4명중 3명은 커피 1명은 치킨
print(type(winners))

print(" -- Congratulation -- ")
print("Chicken: {0}".format(winners[0]))
print("Coffe: {0}".format(winners[1:4]))
print("Congratulation")
