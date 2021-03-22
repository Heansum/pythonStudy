import random

dice = 0
diceCount = 0

while True:
    dice = random.randint(1, 8)
    diceCount += 1

    print("dice = %d / diceCount = %d" % (dice, diceCount))

    if dice == 5 or diceCount == 8:
        break