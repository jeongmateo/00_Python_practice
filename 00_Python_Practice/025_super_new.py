class Unit:
    def __init__(self):
        print("유닛 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()      # 상속받는 순서에 영향을 받는다.
        Unit.__init__(self)
        Flyable.__init__(self)


# 드랍쉽
dropship = FlyableUnit()
