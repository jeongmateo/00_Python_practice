def open_account():
    print("함수가 생성되었 습니다.")


open_account()


def deposit(balance, money):    # 입금
    print("입금이 완료되었습니다, 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):  # 출금
    if balance >= money:  # balance 가 money보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance-money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액은 {0} 원 입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁 출금
    commission = 100
    if balance-money-commission >= 0:
        return commission, balance - money - commission
    else:
        print("잔액이 부족합니다. 현재 잔액은 {0} 원 입니다.".format(balance))
        return commission, balance


balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 900)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))
