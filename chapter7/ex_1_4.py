'''
함수를 정의하는 방법
def 함수이름(매개변수):
    코드1
    코드2
    ...
    코드N

매개변수 - 함수가 동작하는데 필요한 재료
매개변수가 있는 함수
'''

# 1 더하기 1의 결과를 출력하는 함수
def add():
    print(1 + 1)

# 두 수를 더한 결과를 출력하는 함수
# 매개 변수 필요
def add(num1, num2):
    print(num1 + num2)


# 함수를 호출할 때 매개변수 자리에 넣는 값을 인자 라고 부름
# 1, 1 두개의 인자를 넣어서 add 함수 호출
# add(1, 1)

'''
태어난 연도를 입력 받아
나이를 계산해
출력하는 함수를 만드세요
'''
"""
"""

def calcAge(year):
    """
    docString - 함수를 설명하는 주석
    :param year: 태어난 연도
    :return: 없음 # 결과를 만들어냄
    """
    age = 2021 - year
    print("%d 년도생은 나이가 %d살입니다." % (year, age))

print("태어난 년도를 입력하세요 ", end="")
year = int(input())

calcAge(year)



