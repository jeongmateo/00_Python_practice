# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

from random import *


customer = list(range(1, 51))
cut = 0

print(customer)

for i in customer:
    take_time = randrange(5, 51)
    if 5 < take_time < 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, take_time))
        cut += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, take_time))
print("총 탑승 승객 : {0}분".format(cut))
