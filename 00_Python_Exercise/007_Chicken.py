chicken = 10
waiting = 1  # 대기번호 1부터 시작


class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


while(True):
    print("[남은 치킨 : {0}]".format(chicken))

    try:
        if chicken <= 0:
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")

        order = int(input("치킨 몇 마리 주문 하시겠습니까? "))
        # if order <= 0:
        #     raise OrderError("0마리 이하는 입력이 불가 합니다.")

        if order > chicken:
            print("재료가 부족합니다. 현재 남은 치킨은 {0} 마리 입니다.".format(chicken))
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료 되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
    except ValueError:
        print("잘못된 값을 입력 하셨습니다.")
    except SoldOutError as err:
        print(err)
        break
