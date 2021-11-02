class Unit:
    def __init__(self, name, hp, damage):   #객체가 만들어 질 때 자동으로 호출(생성자)
        self.name = name    # Member 변수
        self.hp = hp
        self.damage = damage

        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

# marine1 = Unit("마린",40,5) #Unit class의 instance
# marine2 = Unit("마린",40,5)
# tank = Unit("탱크",150,35)

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스",80,5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage)) 

# 마인드 컨트롤

wraith2 = Unit("레이스",80,5)
wraith2.clocking = True     # class 외부에서 원하는 변수 생성 가능, 생성한 객체에서만 사용가능

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))