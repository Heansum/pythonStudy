# format 메서드
# 메서드 -> input, print와 같은 기능을 의미

data = "Breakfast is {} and {}".format("meal", "eggs")
print(data)

print("My name is {}".format("James"))

print("My name is {0} and {1}".format("James", 25))

print("My name is {1} and {0}".format("James", 25))

print("===== =====")

print("My name is", "James", "and", 25)
print("My name is %s and %d" % ("James", 25))
print("My name is {} and {}".format("James", 25))

# f-string
# 파이썬 3.6 이후로 나온 새로운 기술
# format 메서드와 비슷하지만
# format 메서드 보다 코드 가독성을 더 높일 수 있음

who = "You"
how = "happy"
print(f"{who} make me {how}")

age = 24
print(f"내년엔 {age+1}살이 됩니다.")


