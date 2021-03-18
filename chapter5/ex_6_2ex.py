# 1 ~ 10 까지 모든 수를 갖고 있는 Range
range1 = range(1, 11, 1)    # == range(1,11)
range2 = range(1, 11)


# 10 ~ 1 까지 모든 수를 갖고 있는 Range
range3 = range(10, 0, -1)

range1ToList = list(range1)
range3ToList = list(range3)

print(range1ToList)
print(range3ToList)