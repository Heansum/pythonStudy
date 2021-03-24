'''
내장함수 : 프로그래밍 언어를 개발한 사람들이 만들어놓은 함수
print, input, list, range, set
언어에 내장되어있으므로 별도의 처리 없이 바로 사용 가능
'''

'''
사용자정의함수 : 나와 같은 개발자가 필요에 의해 만든 함수
언어에 내장되어있지 않으므로 별도의 처리(import) 가 먼저 필요함
random
직접 만든 함수도 포함
'''

import random

random.randint()
random.choice()


def add(num1, num2):
    print(num1 + num2)

add(1, 1)

