# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):       # 생성자
        self.name = name
        self.hp = hp
        self.speed = speed

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다.".format(self.name, location))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다.".format(name, location))

class FlyableAttackUnit(AttackUnit, Flyable):
    AttackUnit.__init__(self, name, hp, damage)
    Flyable.__init__(self, flying_speed)




marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

print("유닛이름 : {0}".format(tank.name))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking==True:
    print("{0}은 현재 클로킹 상태입니다.".format(wraith2.name))