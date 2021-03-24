# 하나의 return만 사용해서
# 사용자가 원하는 연산 결과를 반환하도록 하세요.

def calc(num1, num2, cal):
    result = 0

    if cal == "+":
        result = num1 + num2
    elif cal == "-":
        result = num1 - num2
    elif cal == "*":
        result = num1 * num2
    elif cal == "/":
        result = num1 / num2
    else:
        print("연산자를 잘못 입력하셨습니다. ")

    return result


print("첫 번째 수 ", end= "")
num1 = int(input())

print("두 번째 수 ", end= "")
num2 = int(input())

print("연산자 (+, -, *, /) : ", end="")
cal = input()


result = calc(num1, num2, cal)

print("첫 번째 수와 두 번째 수의 연산 결과는", result, "입니다.")