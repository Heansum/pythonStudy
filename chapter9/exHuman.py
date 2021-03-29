class Human:
    def __init__(self):
        self.nose = 1
        self.eye = 2
        self.mouse = 1
        self.ear = 2

        self.arm = 2
        self.leg = 2
        self.finger = 10
        self.toes = 10

        self.name

    def move(self):
        print(self.name, "이(가) 이동합니다.")

    def eat(self):
        print(self.name, "이(가) 먹습니다.")

    def speak(self):
        print(self.name, "이(가) 말합니다.")

    def sleep(self):
        print(self.name, "이(가) 잡니다.")




# person1 객체 (참조변수) object ( Reference variable )
person1 = Human()
# person2 객체 (참조변수)
person2 = Human()

person1.name = "사람1"
person2.name = "사람2"

person1.eat()


