# 출력 시 자릿수 지정 -> 잘 쓰이지 않음
#print("%5d" % 1)
#print("%5d" % 22)
#print("%5d" % 333)
#print("%5d" % 4444)
#print("%5d" % 55555)

# 형식 지정자를 사용한 실습 -> 코드 가독성을 높임!!
name = "Kai"
print("내 이름은 %s 입니다." % name)

print("내 이름은 ", name, "입니다.")

height = 120.5
print("내 키는 %f입니다." % height)
