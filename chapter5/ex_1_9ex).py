#       0123456789
text = "Life is too short, You need Python"

print(text[6])
print(text[13])
print(text[9])
print(text[15])
print(text[16])

print(text[-1])
print(text[-2])
print(text[-9])

text = "python is easy"
print(text[-4])
print(text[-3])
print(text[-2])
print(text[-1])

# 양수 인덱스 번호와 음수 인덱스 번호를 적절히 사용해서
# 아래와 같이 출력하세요
# python
word1 = text[0] + text[1] + text[2] + text[3] + text[4] + text[5]
print(word1)

# is
word2 = text[-7] + text[-6]
print(word2)

# easy
word3 = text[-4] + text[-3] + text[-2] + text[-1]
print(word3)