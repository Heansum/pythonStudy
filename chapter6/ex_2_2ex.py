print("숫자를 입력하세요 ", end="")
num = input()
num = int(num)

if num % 2 == 0:
    print("2 * 1 = ", 2 * 1)
    print("2 * 2 = ", 2 * 2)
    print("2 * 3 = ", 2 * 3)
    print("2 * 4 = ", 2 * 4)
    print("2 * 5 = ", 2 * 5)
    print("2 * 6 = ", 2 * 6)
    print("2 * 7 = ", 2 * 7)
    print("2 * 8 = ", 2 * 8)
    print("2 * 9 = ", 2 * 9)

else:
    print("3x1=3")
    print("3x2=6")
    print("3x3=9")
    print("3x4=12")
    print("3x5=15")
    print("3x6=18")
    print("3x7=21")
    print("3x8=24")
    print("3x9=27")

print("두 수를 입력하세요 ", end="")
num1 = int(input())
num2 = int(input())

if num1 > num2:
    print(num1)

else:
    print(num2)

print("세 수를 입력하세요 ", end="")
num3 = int(input())
num4 = int(input())
num5 = int(input())

if num3 > num4:
    if num3 > num5:
        print(num3)
    else:
        print(num5)
else:
    if num4 > num5:
        print(num4)
    else:
        print(num5)


