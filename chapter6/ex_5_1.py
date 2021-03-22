# 반복문 - continue
# break 문과 마찬가지로 반복문의 안에서 흐름을 조절할 때 사용
# 특정 코드 뭉치들을 실행하지 않고 다시 조건을 비교하고자 할때

i = 0

add = 0

while i < 100:
    i = i + 1

    if i % 2 == 0:
        continue

    add = add + i


print(add)


