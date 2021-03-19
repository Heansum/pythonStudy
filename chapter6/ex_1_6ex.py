print("미세먼지 농도를 입력하세요 : ", end="")
dust = input()
dust = int(dust)


if dust >= 5:
    print("마스크를 쓰고 나간다")

    print("얼마 있습니까? ", end="")
    money = input()
    money = int(money)

    if money >= 10000:
        print("택시를 탄다")

    if money < 10000:
        print("걸어간다")

if dust < 5:
    print("마스크를 쓰지 않고 나간다")
    
    print("얼마 있습니까? ", end="")
    money = input()
    money = int(money)
    
    if money >= 2000:
        print("지하철을 탄다")
    
    if money < 2000:
        print("걸어간다")
