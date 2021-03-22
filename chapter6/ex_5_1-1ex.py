num = int(input())

if num == 0:
    print("프로그램 종료")
elif num > 0:
    while num >= 1:
        if num % 3 != 0:
            print(num)

        num -= 1
elif num < 0:
    while num <= 1:
        if num % 3 != 0:
            print(num)

        num += 1


