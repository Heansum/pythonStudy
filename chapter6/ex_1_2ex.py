print("오늘의 미세먼지 농도를 입력하세요")

findust = input()
findust = int(findust)
if findust >= 5:
    print("마스크를 쓰고 나간다")


if findust < 5:
    print("마스크를 쓰지 않는다")

print("얼마 있습니까?")

money = input()
money = int(money)

if money >= 10000:
    print("grab the taxi")

elif money <10000:
    print("foot road")