print("X = ", end="")
x = int(input())
print("Y = ", end="")
y = int(input())

# if문만 사용했을 때와 if elif else 를 같이 사용했을 때의 차이는?
if x > y:
    print("X가 큽니다")
elif x < y:
    print("X가 작습니다")
else:
    print("X와 Y가 동일합니다")

print("============")

if x > y:
    print("X가 큽니다")
if x < y:
    print("X가 작습니다")
if x == y:
    print("X와 Y가 동일합니다")

# if 문은 다 실행
# if elif문은 둘 중 참일경우 통과
# if elif는 참일경우 통과 하기 때문에 연산이 적어지고 소스코드가 최적화된다!!
