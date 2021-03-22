print("얼마 있습니까")

money = int(input())
mixCoffeAmount = 10
price = 300

while True:
    mixCoffeAmount -= 1
    money = money - price

    if mixCoffeAmount == 0:
        print("믹스커피가 부족합니다. 반환되는 잔액은 %d 원입니다" % money)
        break

    if money < price:
        print("잔액이 부족합니다. 반환되는 잔액은 %d 원입니다" % money)
        print("믹스커피의 여분은 %d개입니다" % mixCoffeAmount)
        break


