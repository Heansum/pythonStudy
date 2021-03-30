class A:
    def print(self):
        print("A")

class B(A):
    pass

class C(B):
    def print(self):
        print("C")

# 상속 관계에서 부모클래스로부터 물려받은 메서드를
# 자식 클래스에게 맞게 구현을 바꾸는 것 -> 오버라이딩
# 자식 클래스가 오버라이딩을 하려면 메서드의 정의 부분은 똑같이
# 하고 구현만 다르게 해야함

a = A()
b = B()
c = C()


