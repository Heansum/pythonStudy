'''
함수를 만드는 방법 (정의, 선언)
def 함수이름(매개변수):
    코드1
    코드2
    ...
    코드N
    
매개변수 - 함수가 동작하는데 필요한 재료
매개변수는 있을수도 있고 없을수도 있음
'''

def sayHello():
    print("Hello")


# sayHello 라는 이름의 함수를 호출
# 함수를 호출할 때 ( ) 는 매개변수 자리
# sayHello 함수를 정의할 때 매개변수를 비워뒀으므로
# 함수를 호출할 때도 매개변수 자리는 비워둔다.
#sayHello()

def welcome():
    print("Hello Python")
    print("Nice to meet you")
    print("=" * 10)


for i in range(3):
    print("Hello Python")
    print("Nice to meet you")
    print("=" * 10)

for i in range(3):
    welcome()

