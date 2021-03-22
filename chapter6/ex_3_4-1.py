import random

nansu = [False, False, False, False, True, False, False, False, False]
cutDown = False
hit = 0

while True:
    cutDown = random.choice(nansu)

    if cutDown :
        print("나무를 쓰러트렸다.")
    else :
        hit += 1
        print("나무를 {0}번 찍었다".format(hit))

    if cutDown != True:
        print("나무를 쓰러트리지 못했습니다.")
        break


