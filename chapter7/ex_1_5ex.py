# 매개변수 -> 함수를 연결 시킨다
# connect
def compare(num1, num2):
    """
    
    :param num1: 1번 값 
    :param num2: 2번 값
    :return: 없음
    """
    if (num1 > num2):
        print(num1)
    else:
        print(num2)

# 두 정수 중 작은 수를 출력하는 함수를 만드세요.
def compare1(num1, num2):
    if (num1 > num2):
        print(num2)
    else:
        print(num1)

# 세 정수 중 큰 수를 출력하는 함수를 만드세요.
# 1 2 3
# 1 3 2 1
# 2 1 3
# 2 3 1 2
# 3 1 2
# 3 2 1 3
# 내가 한 풀이
def maximum(num1, num2, num3):
    if (num1> num2 > num3):
        print(num1)
    elif (num1 > num3 > num2):
        print(num1)
    elif (num2 > num1 > num3):
        print(num2)
    elif (num2 > num3 > num1):
        print(num2)
    elif (num3 > num1 > num2):
        print(num3)
    elif (num3 > num2 > num1):
        print(num3)
#
# answer
def maximum(num1, num2, num3):
    # max - 큰 수
    max = num1

    if num2 > max:
        max = num2
    if num3 > max:
        max = num3
        
    print("최대값은 ", max, " 입니다")

# 네 정수 중 큰 수를 출력하는 함수를 만드세요.
def maximun4(var1, var2, var3, var4):
    # max - 큰 수

    max = var1

    if var2 > max:
        max = var2
    if var3 > max:
        max = vars3
    if var4 > max:
        max = var4

    print(max)

num1 = 10
num2 = 20
num3 = 30
num4 = 40

maximun4(num1, num2, num3, num4)

def swap(var1, var2):
    temp = var1
    var1 = var2
    var2 = temp


num1 = 10
num2 = 20

swap(num1, num2)





compare(1, 2)
compare(2, 1)

def define(var):
    """
    
    :param var: 입력값
    :return: 없음
    """
    if (var % 2 == 0):
        print("짝수")
    else:
        print("홀수")

define(1)
define(2)

print("성적을 입력하세요 ")
kor = int(input())
eng = int(input())
math = int(input())

def student(kor, eng, math):
    """
    
    :param kor: 입력받는 국어 값 
    :param eng: 입력받는 영어 값
    :param math: 입력받는 수학 값
    :return: 없음
    """
    total = kor + eng + math
    avg = total / 3.0
    print("총합은 = %d" % total)
    print("평균은 = %f" % avg)

student(kor, eng, math)

