
# 마트 카트

class Cart():
    def __init__(self, width, height, frame, wheel):
        self.width = width
        self.height = height
        self.frame = frame
        self.wheel = wheel
        self.goodsList = []
        self.nowPosition = {"x": 0, "y": 0}


    def move(self, x, y, speed):
        if(x > 0):
            movedX = x * speed
            print("카트를 x축으로 {0}의 속도로 {1}만큼 움직임".format(speed, movedX))
            self.nowPosition["x"] += movedX

        if (y > 0):
            movedY = y * speed
            print("카트를 x축으로 {0}의 속도로 {1}만큼 움직임".format(speed, movedY))
            self.nowPosition["y"] += movedY

    def putIn(self, goods):
        self.goodsList.append(goods)
        print("카트에 {}을 담았습니다".format(goods))

    def putOut(self, goods):
        self.goodsList.remove(goods)
        print("카트에 {}을 뺍니다".format(goods))

    def info(self):
        print(self.width)
        print(self.height)
        print(self.wheel)
        print(self.goodsList)


# 연관있는 데이터를 묶어주는 것 - 클래스


# 마트 카트

groceriesCart = Cart(100, 200, "철제", 4)
EmartCart = Cart(20, 50, "스탠", 4)
ironCart = Cart(300, 200, "철제", 6)
woodCart = Cart(200, 300, "나무", 2)


groceriesCart.width = 120
groceriesCart.frame = "알루미늄"

groceriesCart.move(10, 10, 1)

groceriesCart.putIn("앙파")
groceriesCart.putIn("무")
groceriesCart.putIn("마늘")
groceriesCart.putIn("김치")

groceriesCart.putOut("앙파")

print(groceriesCart.goodsList)
groceriesCart.info()



