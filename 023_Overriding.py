# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):  # 객체가 만들어 질 때 자동으로 호출(생성자)
        self.name = name    # Member 변수
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))
# 공격 유닛


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):  # 객체가 만들어 질 때 자동으로 호출(생성자)
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}"
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} 유닛이 파괴 되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기, 마린 /파이어뱃 / 탱크 등을 수송

# 날 수 있는 기능을 가진 Class


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed는 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중유닛 이동]")
        self.fly(self.name, location)


# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀쿠루져
BattleCruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

vulture.move("11시")
BattleCruiser.move("9시")
