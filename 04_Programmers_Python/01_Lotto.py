def solution(lottos, win_nums):
    count = 0
    lottos_max = 0

    # count 0 int lottos & remove that element
    while 0 in lottos:
        lottos.remove(0)
        count = count + 1

    # change the type for set() , because of compare lottos and win_nums more easily 
    lottos = set(lottos)
    win_nums = set(win_nums)

    # Check the matching count & exception handler(in case of over the number six)
    if len(lottos & win_nums)+count >= 6:
        lottos_max = 6
    else:
        lottos_max = len(lottos & win_nums)+count

    answer = [switch(lottos_max),switch(len(lottos & win_nums))]
    return answer

# matching the rank by dictionary
def switch(key):
    return {6:1,5:2,4:3,3:4,2:5,1:6,0:6}.get(key)

# EX)
lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos,win_nums))