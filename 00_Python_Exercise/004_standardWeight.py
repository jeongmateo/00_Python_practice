
def standardWeight(height, gender):
    if gender == "남자":
        return(round((height * height * 22), 2))
    else:
        return(round((height * height * 21), 2))


height = float(input("키를 입력하세요(m): "))
gender = input("성별을 입력하세요(Ex. 남자/여자): ")

print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다".format(
    height*100, standardWeight(height, gender)))
