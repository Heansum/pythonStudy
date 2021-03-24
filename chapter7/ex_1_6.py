'''
함수를 정의하는 방법
def 함수이름(매개변수):
    소스코드1
    소스코드2
    ...
    소스코드N
'''

# 1 더하기 1을 출력하는 함수를 만드세요
def add0():
    print(1 + 1)

#return 이 포함된 함수
# 두 수를 더한 결과를 출력하는 함수를 만드세요
def add2(num1, num2):
    return num1 +num2

# 두 정수 중 큰 수를 반환하는 함수를 만드세요.
def maximum(num1, num2):
    max = num1
    if num2 > max:
        max = num2

    return max

    # 실행되지 않는다 -> return 뒤에 있기 때문에
    print("maximum함수의 끝")

# 두 정수 중 작은 수를 반환하는 함수를 만드세요.
def minimum(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

    # return num1 -> 돌아감
    # return num2 -> 절대 실행되지않음


# 세 정수 중 가운뎃 수를 반환하는 함수를 만드세요.
def mid3(num1, num2, num3):
    if num1 >= num2:
        if num2 >= num3:
            return num2
        elif num1 <= num3:
            return num1
        else:
            return num3
    elif num1 > num3:
        return num1
    elif num2 > num3:
        return num3
    else:
        return num2

# 국, 영, 수 점수를 전달받아 합계와 평균을 반환하는 함수를 만드세요
def calcScore(kor, eng, mat):
    sum = kor + eng + mat
    avg = sum / 3.0

    # 합계와 평균을 반환하는 return 문을 완성하세요.
    return {"합계": sum, "평균": avg}


result = calcScore(1, 2, 3)
print(result["합계"])
print(result["평균"])



result = add1()
print("add1 함수의 결과값 = ", result)

print("add2 함수의 결과값 = ", add2(1, 1))



