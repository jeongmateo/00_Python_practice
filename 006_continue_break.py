absent = [2, 5]  # 결석
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
        break
    print("{0}야 책을 읽어보렴".format(student))
