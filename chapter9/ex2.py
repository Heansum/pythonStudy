'''
게임 캐릭터에게 필요한
속성 - 체력, 마력, 물리공격력, 마법공격력, ...
기능 - 물리공격, 마법공격, 이동, ...
'''
import playableCharacter as PC
import NonPlayableCharacter as NPC

print("공격 받기 전 monsterHP = ", NPC.monsterHP)

# 전사 캐릭터가 몬스터를 공격한다.
NPC.monsterHP = PC.attack(NPC.monsterHP, PC.warriorPhysicalAttackPower)

print("공격 받은 후 monsterHP")


# 전사 캐릭터가 몬스터 캐릭터를 공격한다.

def attack(monsterHP, 물리공격력):
    print("attack 함수 안")

    # 공격을 하기 위한 모션 (그래픽처리)

    monsterHP = monsterHP - 물리공격력
    print(monsterHP)
    # 공격을 받은 모션 (그래픽처리)

# 전사 캐릭터
warrior = Character()
warriorHP = 100
warriorMP = 50
warrior.물리공격력 = 15.7
warrior.마법공격력 = 5

# 궁수 캐릭터
archer = Character()
archer.Hp = 70
archer.MP = 70
archer.물리공격력 = 7
archer.마법공격력 = 7


archer.Hp =warrior.attack(archer.Hp)

warrior.Hp = archer.attack(warrior.Hp)

# 몬스터 캐릭터
monsterHP = 175
monsterMP = 0
monsterPhysicalAttackPower = 5
monsterMagicalAttackPower = 1

print("공격 받기 전 monsterHP = ", monsterHP)

# 전사 캐릭터가 몬스터를 공격한다.
attack(monsterHP, warriorPhysicalAttackPower)

print("공격 받은 후 monsterHP")


# 공격을 받은 모션 (그래픽처리)

def move():
    pass

def say():
    pass

def buy():
    pass

def exit():
    pass

def monsterMove():
    pass





