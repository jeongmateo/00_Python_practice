# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t 사용언어 : {2}".format(name, age, main_lang))


# profile("정한수", 30, "파이썬")
# profile("강나현", 27, "자바스크립트")

# 같은 학교 같은 학년 같은 반 같은 수업

def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t사용언어 : {2}".format(name, age, main_lang))


profile("정한수")
profile("강나현")
