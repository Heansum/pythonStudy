# 국어 성적을 입력 받는 부분
print("국어 성적: ", end="")
kor = int(input())

print((kor >= 0) and (kor <= 100))

# 0 <= kor < = 100 -> python 에서만 적용
print(0 <= kor <= 100)

# 다른 언어에서
# print(0 <= kor and kor <= 100)

result1 = kor < 0
result2 = kor > 100
result = not(result1 or result2)

print(result)

