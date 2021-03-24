# 내장함수
# abs()
# slice()
# len()
# max()
# round()

# 문자열과 관련된 내장함수
# chr() -> 정수를 문자로 변환하는 함수
# ord() -> 문자를 정수로 변환하는 함수
# eval() -> 문자열로 이루어진 연산을 해주는 함수
# format() -> 데이터를 원하는 형식의 문자열로 변환해주는 함수
# str() -> 데이터를 문자열로 변환해주는 함수

print(chr(48))

print(chr(97))

# chr함수를 사용해서 Z, !를 출력하세요
print(chr(90))

print(chr(33))

print(ord("A"))

print(eval("1 + 1"))

num1 = 27
print(eval("num1 * 2"))


# print("{}".format(5)) -> format method와 format 내장함수는 다르다

print(1000)
print(format(10000, ","))

# print(format(100000, "."))

str(1000)

print("계산식을 입력하세요 : ", end="")
expr = input()

print(expr + " = " + str(eval(expr)))
