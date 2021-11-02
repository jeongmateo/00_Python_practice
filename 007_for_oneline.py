# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101 102 103 104

students = [1, 2, 3, 4, 5]
print(students)

students = [i+100 for i in students]

print(students)

# 학생 이름을 길이로 변환

students = ["hansoo", "nahyun", "jihuyudn"]
students = [len(i) for i in students]
print(students)

students = ["hansoo", "nahyun", "jihuyudn"]
students = [i.upper() for i in students]
print(students)

students = ["HANSOO", "nahyun", "jihuyudn"]
students = [i.lower() for i in students]
print(students)
