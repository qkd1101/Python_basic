class Unit :
    def __init__(self,name,hp) : #Python의 생성자
        self.name = name #멤버변수
        self.hp = hp
 
class AttackUnit(Unit):
    def __init__(self,name,hp,damage) : #Python의 생성자
            Unit.__init__(self,name,hp) #상속받은 클래스
            self.damage = damage

class Flyable :
    def __init__(self,flying_speed) :
        self.flying_speed = flying_speed

    def fly(self,name,location) :
        print("{0} : {1}".format(name,location)) #self 안 썻음

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__( self,name,hp,damage,flying_speed) :
        AttackUnit.__init__(self,name,hp,damage)
        Flyable.__init__(self,flying_speed)

Valkyrie = FlyableAttackUnit("Valkyrie",200,6,5)
Valkyrie.fly(Valkyrie.name,10)