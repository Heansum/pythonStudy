# set -> 집합이라는 뜻
# 리스트,튜플과 마찬가지로 데이터들을 저장할 수 있는 데이터 타입
# 원소의 순서는 고려사항이 아니다

# 변수명 = {값,값,값,...}
# set = {요소,요소,요소,...}
# dic = {key:value, key:value}

numberSet = {1, 2, 1, 3}

stringSet = {"파", "이", "이", "썬"}

print(numberSet)
print(stringSet)

numberSet = {1, 2, 3}
emptySet = {}

print(numberSet)
print(emptySet)

print(type(numberSet))
print(type(emptySet))

# 자료형 - set
# 변수명 = {값1, 값2, 값3, ...} or
# 변수명 = set(시퀀스객체)

emptySet = set()
numberSet = set([1, 2, 3])
stringSet = set("파이썬")

print(emptySet)
print(numberSet)
print(stringSet)

print(type(emptySet))
print(type(numberSet))
print(type(stringSet))



