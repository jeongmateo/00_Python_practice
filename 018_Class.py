class Unit:
    def __init__(self, name, hp, damage):   #객체가 만들어 질 때 자동으로 호출(생성자)
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

marine1 = Unit("마린",40,5) #Unit class의 instance
marine2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)
    