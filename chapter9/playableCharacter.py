'''
아래 클래스를 완성하고
Character 클래스를 사용해서 warrior 객체, archer 객체를 만드세요.
'''


class Character:
    # 클래스는 속성을 갖고 있고
    # 캐릭터를 예로들면 속성 - 그 캐릭터를 위한 능력치
    # HP, MP, 물리공격력, 마법 공격력, ...

    # __init__ 라는 메서드 (생성자) 를 정의하고
    # 생성자 안에 클래스가 필요한 속성들을 정의한다.
    # 생성자 메서드는 우리가 호출할 수 없는 메서드
    # 일반적인 attack과도 같은 메서드는 우리가 호출 할 수 있는 메서드
    
    def __init__(self):
        self.HP = 0
        self.MP = 0
        self.물리공격력 = 0.0
        self.마법공격력 = 0.0


    # 클래스 기능을 갖고 있다.
    # 캐릭터를 예로들면 기능 - 공격, 이동, 대화하기, 길드 가입하기, ...
    # 클래스 바깥에 기능이 정의되어 있으면 - 함수
    # 클래스 안에 기능이 정의되어 있으면 - 메서드

    # 메서드는 첫 번째 매개변수가 반드시 필요하다.
    # 메서드의 첫 번재 매개변수 이름은 self를 사용한다.
    # 매개변수가 필요하지 않은 메서드라도 반드시 첫 번째 매개변수인 self를 넣어줘야한다

    def attack(self, target):
        print("attack 함수 안")

        # 공격을 하기 위한 모션 (그래픽처리)

        target.HP = target.HP - self.물리공격력

        # 공격을 받은 모션 (그래픽처리)

        # 리턴 안써도됨 이젠
        
    def move(self):
        pass

    def say(self):
        pass

    def buy(self):
         pass

    def exit(self):
        pass

    def monsterMove(slef):
        pass

        # 플레이어블 캐릭터 틀을 만들어 놓고
        # 그 틀을 사용해서

# 전사 캐릭터
warrior = Character()
warriorHP = 100
warriorMP = 50
warrior.물리공격력 = 15.7
warrior.마법공격력 = 5


# 궁수 캐릭터
archer = Character()
archer.HP = 70
archer.MP = 70
archer.물리공격력 = 7
archer.마법공격력 = 7

warrior.attack(archer)
print(archer.HP)

archer.attack(warrior)
print(warrior.HP)



# 클래스
# 과자 틀만 있으면 똑같은 모양의 과자를 계속 만들 수 있듯이
# 클래스만 있다면 똑같은 속성과 기능을 갖고 있는 객체를 계속 만들 수 있다.
# class 클래스명:
#   요소
#   기능


# 전사 캐릭터가 몬스터 캐릭터를 공격한다.

'''
def attack(monsterHP, warriorPhysicalAttackPower):
    print("attack 함수 안")

    # 공격을 하기 위한 모션 (그래픽처리)

    monsterHP = monsterHP - self.물리공격력
    print(monsterHP)
    # 공격을 받은 모션 (그래픽처리)



print("공격 받기 전 monsterHP = ", monsterHP)

# 전사 캐릭터가 몬스터를 공격한다.
attack(monsterHP, 물리공격력)

print("공격 받은 후 monsterHP")
'''

# 공격을 받은 모션 (그래픽처리)

def move(self):
    pass

def say(self):
    pass

def buy(self):
    pass

def exit(self):
    pass

def monsterMove(slef):
    pass

# 플레이어블 캐릭터 틀을 만들어 놓고
# 그 틀을 사용해서
# 전사의 능력치를 갖고 있는 캐릭터
# 궁수의 능력치를 갖고 있는 캐릭터
# 찍어낼 수 있음

# 전사 캐릭터
warriorHP = 100
warriorMP = 50
warriorPhysicalAttackPower = 15.7
warriorMagicalAttackPower = 5

archerHP = 75
archerMP = 75
acrcherPhysicalAttackPower = 17
