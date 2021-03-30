class PersonFaceInfo:
    def __init__(self, eye, nose, mouth):
        self.eye = eye
        self.nose = nose
        self.mouth = mouth

class PersonBodyInfo:
    def __init__(self, finger, toe, leg):
        self.finger = finger
        self.toe = toe
        self.leg = leg


# 사람은 눈, 코, 입, 손가락, 발가락, 다리를 갖고 있고
# 숨쉬고, 먹고, 말하기를 할 수 있다.
class Person:
    def __init__(self, eye, nose, mouth, finger, toe, leg):
        # 얼굴과 관련된 데이터
        self.personFaceInfo = PersonFaceInfo(eye, nose, mouth)
        # 몸과 관련된 데이터
        self.personBodyInfo = PersonBodyInfo(finger, toe, leg)

    def showInfo(self):
        print(self.personFaceInfo.eye)
        print(self.personFaceInfo.nose)
        print(self.personFaceInfo.mouth)
        print(self.personBodyInfo.finger)
        print(self.personBodyInfo.toe)
        print(self.personBodyInfo.leg)



    def breath(self):
        print("숨쉬기")
        
    def eat(selfs):    
        print("먹기")
        
    def say(self):
        print("말하기")

class PersonStudent(Person):
    def __init__(self, eye, nose, mouth, finger, toe, leg):
        # 얼굴과 관련된 데이터
        self.personFaceInfo = PersonFaceInfo(eye, nose, mouth)
        # 몸과 관련된 데이터
        self.personBodyInfo = PersonBodyInfo(finger, toe, leg)





person1 = Person(2, 1, 1, 10, 10, 2)
person1.showInfo()
person1.breath()


# 학생은 사람의 특징을 갖고 있으면서 신분이 학생이다
# 학생은 사람의 기능을 하면서 공부도 할 수 있다.
personStudent1 = PersonStudent(2, 1, 1, 10, 10, 2)
personStudent1.breath()

# 모든 클래스의 최상위 부모 클래스는 Object 클래스임
# 다형성 : 한 클래스가 시점에 따라서 상속 받은 부모 클래스가 될 수 있다.




