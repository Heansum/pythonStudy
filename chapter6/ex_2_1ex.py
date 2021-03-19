print("오늘의 미세먼지 농도를 입력하세요 ", end="")

findDust = int(input())

if findDust >= 5:
    print("집에 있는다.")

else:
    print("밖에 나간다.")

print("얼마 있습니까? ", end="")

money = int(input())

if money >= 10000:
    print("택시를 탄다")

else:
    print("버스를 탄다")
    
print("비가오면 1 아니면 0을 입력하세요 ", end="")

Rain = bool(input())

if Rain:
    print("우비를 입고 나간다")
    
else:
    print("선글라스를 쓴다")