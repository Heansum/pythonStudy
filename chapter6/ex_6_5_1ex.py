
print("줄 수 = ", end= "")
row = int(input())

for rowCount in range(1, row+1):
    print("*" * rowCount)

for rowCount in range(1, row+1):
    for columnCount in range(1, rowCount+1):
        print("*", end="")

    print()

# 집에서 복습하자! 개발 중에서 가장어려운 난이도 코드 이다.
# 강사님) 이 정도 하면 실무에서 빅데이터 인공지능 다 배울 수 있다.



