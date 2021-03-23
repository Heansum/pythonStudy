def plus():
    print(1+1)

plus()

def gugudan():
    forward = 2
    for backward in range(1,10):
            print("%d * %d = %d" % (forward, backward, forward * backward))

gugudan()

def choose():

    num = 17
    if (num % 2 == 0):
        print("짝수")
    else:
        print("홀수")

choose()
