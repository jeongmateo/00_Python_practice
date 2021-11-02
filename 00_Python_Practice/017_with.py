# import pickle

# # with문을 탈출하면서 Close는 자동으로 해준다.
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

with open("study.txt","r", encoding="utf8") as study_file:
    print(study_file.read())