import random

# 주사위를 한번 굴림
dice = random.randint(1, 6)
print(dice)

dice = random.randint(1, 6)
print(dice)

dice = random.randint(1, 6)
print(dice)

dice = 0

while dice != 4:
    dice = random.randint(1, 6)
    print("dice = %d" % dice)

dice = [1, 2, 3, 4, 5, 6]
nansu = 0

while nansu != 4:
    nansu = random.choice(dice)
    print("dice = %d" % nansu)

