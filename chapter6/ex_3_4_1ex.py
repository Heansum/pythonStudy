print("교통카드에 얼마 충전 하겠습니까 ", end="")
money = int(input())
price = 1350

while money >= price:       # money 가 price 이상이여야 차감가능
    # break 키워드를 만나는 순간
    # break 키워드가 속한 반복문에서 빠져나감
    if money < price:
        break


    money = money - price

    print("잔액 : %d " % money)

print("프로그램 종료")

