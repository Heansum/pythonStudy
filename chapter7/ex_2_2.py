# 두 정수 중 최대값을 구하세요.
maximum = max(1, 10)
print(maximum)

numberList = [1, 3, 7, 10, 2, 8, 9]
maximum = max(numberList)
print(maximum)

# range, list, tuple, len
# sorted 함수 - 오름차순 정렬
print("정렬 전")
print(numberList)

print("정렬 후")
print(sorted(numberList))

# 오름차순 정렬 함수
testList = [2, 1, 3, 5, 4, 6, 9, 8, 7, 10, 11]

# 이 반복문의 한계는?
for i in range(1, len(testList)):
    if testList[i-1] > testList[i]:
        temp = testList[i]
        testList[i] = testList[i-1]
        testList[i-1] = temp

'''
if testList[1] > testList[2]:
    temp = testList[2]
    testList[2] = testList[1]
    testList[1] = temp

if testList[2] > testList[3]:
    temp = testList[3]
    testList[3] = testList[2]
    testList[2] = temp

if testList[3] > testList[4]:
    temp = testList[4]
    testList[4] = testList[3]
    testList[3] = temp
'''

print(testList)



