# c언어에는 클래스가 없다
# 이말은 굳이 클래스가 없어도 프로그래밍 가능하다는 것
# 꼭 필요한 요소는 아니지만 사용하면 프로그래밍에 날개를 달아준다
'''
number1, number2, op, result : 계산기를 위한 변수
add, minus, div, mul : 계산기를 위한 함수

연관있는 변수와 연관있는 함수를 하나로 묶는 방법: 클래스

클래스로 묶은 변수 - 요소, 속성, 멤버 변수
클래스로 묶은 함수 - 기능, 함수, 멤버 메서드
'''

# Calculator 클래스를 정의했다. 선언했다.
class Calculator:
    # 계산기를 위한 클래스
    # 속성 - 값1, 값2, 연산자, 연산 결과, ...
    def __init__(self):
        self.num1
        self.num2
        self.op
        self.result
        self.color
        self.brand

    # 기능 - 더하기, 빼기, 곱하기, 나누기, ...
    def add(num1, num2):
        return num1 + num2

    def minus(num1, num2):
        return num1 - num2


# Calculator() -> 클래스의 인스턴스를 만든다.
# 클래스의 인스턴스를 만든다. -> 쿠키 틀은 먹을 수 없고, 쿠키 틀로 찍어낸 쿠키를 먹을 수 있는것처럼
# 클래스를 정의해뒀다고 해서 그 클래스를 사용할 수 있는건 아님
# 클래스의 인스턴스를 만들어야지 클래스 안에 정의해둔 속성(멤버 변수)과 기능(멤버 메서드)을
# 사용할 수 있다.

# redCal 객체
redCal = Calculator()
redCal.num1 = 10
redCal.num2 = 24
redCal.add(1, 1)

# blueCal 객체
blueCal = Calculator()
blueCal.color = "blue"
blueCal.add(1, 2)

# blackCal 객체
blackCal = Calculator()
blackCal.color = "black"





blueCal = Calculator()

blackCal = Calculator()



while True:
    print("===== 계산기 =====")
    print("연산하고자 하는 두 수를 입력 후")
    print("연산자를 입력하세요.")
    print("연산은 +, -, *, / 만 가능합니다.")
    print("프로그램을 종료하려면 연산자에 0을 입력하세요.")
    print("===== ===== =====")


    print("입력1 : ", end="")
    number1 = int(input())

    print("입력2 : ", end="")
    number2 = int(input())

    print("연산자 : ", end="")
    op = input()
    if op == 0:
        break

    if op == "+":
        result = result + (number1 + number2)

    elif op == "-":
        result = result + (number1 - number2)

    print(result)


