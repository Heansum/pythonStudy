# 이동수단의 요소
# me
class vehicle():
    def __init__(self, color, width, height):
        self.wheel = 4
        self.color = color
        self.width = width
        self.height = height

    def move(self, x, y, speed):
        if (x > 0):
            movedX = x * speed
            print("이동수단을 x축으로 {0}의 속도로 {1}만큼 움직임".format(speed, movedX))
            self.nowPosition["x"] += movedX

        if (y > 0):
            movedY = y * speed
            print("이동수단을 y축으로 {0}의 속도로 {1}만큼 움직임".format(speed, movedY))
            self.nowPosition["y"] += movedY

    def info(self):
        print("This is imformation")
        print(self.width)
        print(self.height)
        print(self.wheel)



car = vehicle("red", 10, 20)

train = vehicle("black", 100, 200)

airplane = vehicle("white", 50, 60)

car.info()
train.info()
airplane.info()


# answer
class Transport:
    # 클래스 멤버 변수(속성)
    # 모든 객체가 공유하는 멤버 변수
    passengerList = []

    def __init__(self):
        # 이용 요금 - 1350원
        # 비공개 멤버 변수 - 변수의 이름 앞에 __를 붙인다.
        # 클래스 바깥에서 접근할 수 없는 멤버 변수
        self.__charge = 1350
        # 탑승객 목록
        # 공개 멤버 변수 - 변수의 이름 앞에 별도의 기호가 없다.
        # 클래스 바깥에서도 접근할 수 있는 멤버 변수
        self.passengerList = []
        # 이동 수단의 종류
        self.kind = ""
        # 이동 수단의 바퀴 개수
        self.wheel = 0
        # 이동 수단에 최대 탑승 인원
        self.maximumPeople = 0
        # 이동 수단의 x 위치
        self.x = 0
        # 이동 수단의 y 위치
        self.y = 0

    def move(self, x, y, speed):
        self.x = x * speed
        self.y = y * speed

    def getIn(self, name, fee):
        print("이용 요금은 ", self.__charge, "원 입니다.")
        print("지불하신 금액은 ", fee, "원 입니다.")

        money = fee - self.__charge
        if money > 0:
            print("잔액 ", money, "원이 반환됩니다.")
        else:
            print("잔액이 반환되지 않습니다.")


        self.passengerList.append(name)
        Transport.passengerList.append(name)


bicycle = Transport()
bicycle.getIn("홍길동", 1500)

print("바꾸기 전 이동수단의 요금 = ", bicycle.__charge)
bicycle.__charge = 1500
print("바꾸고 나서의 이동수단의 요금 = ", bicycle.__charge)

vehicle = Transport()
vehicle.getIn("설까치")

motocycle = Transport()
motocycle.getIn("하니")

print(Transport.passengerList)


