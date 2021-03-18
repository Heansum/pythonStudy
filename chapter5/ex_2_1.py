text = "python is easy"

#python
print(text[0:6])
print(text[:6])

#is
print(text[7:9])

#easy
print(text[10:])
print(text[10:14])

text = "Life is too short, You need Python"

# is
print(text[5:7])

# too
print(text[8:11])

#Life is too short,
print(text[:19])

#Life is too short, You need Python
print(text[:])


# 인덱스 번호 하나를 지정해서 접근할 때는 인덱스 범위를 벗어나면 안된다.
print(text[14])

# 다른 경우에는 뒤에 가능
# print(text[10:15])

