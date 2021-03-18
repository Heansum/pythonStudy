simpleText = "apple, banana, pineapple"

print("apple" in simpleText)
print("grape" in simpleText)

print("apple" not in simpleText)
print("grape" not in simpleText)


# 수정 가능한 데이터 타입
# 읽고 쓸 수 있는 데이터 타입
# mutable 데이터 타입
# 리스트, 세트, 딕셔너리

# 수정 불가능한 데이터 타입
# 읽기만 가능한 데이터 타입
# immutable 데이터 타입
# 정수, 실수, 문자열, 튜플

simpleString = "문자열"
simpleList = ["리", "스", "트"]
simpleTuple = ("튜", "플")

simpleString[0] = "1"
simpleList[0] = 1
simpleTuple[0] = 1
