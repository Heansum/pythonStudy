class Animal:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        '''
        비공개 멤버 변수인 name의 값이 필요할 때 호출하는 메서드
        :return: 비공개 멤버 변수 name의 ㄱ밧
        '''
        return self.__name

    def setName(self, name):
        self.__name = name
        '''
        비공개 멤버 변수인 name에 값을 설정할 때 호출하는 메서드
        :param name: 문자열
        :return: 없음
        '''
    
    
    
    def run(self):
        print(self.__name + "이(가) 네발로 달립니다.")
        
class Rabbit(Animal):
    def __init__(self, name):
        setName(name)

class Person(Animal):
    def __init__(self, name):
        setName(name)

    def run(self):
        print("사람이 달립니다")


rabbit = Rabbit("토끼")
rabbit.run()

person = Person("사람")
person.run()


    
