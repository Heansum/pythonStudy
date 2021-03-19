leftSet = set("나는 오늘도 파이썬을 공부한다")
rightSet = set("나는 내일도 파이썬을 공부한다")

print(leftSet & rightSet)
print(leftSet.intersection((rightSet)))


leftSet = set("나는 오늘도 파이썬을 공부한다")
rightSet = set("나는 내일도 파이썬을 공부한다")

print(leftSet | rightSet)
print(leftSet.union((rightSet)))


leftSet = set("나는 오늘도 파이썬을 공부한다")
rightSet = set("나는 내일도 파이썬을 공부한다")

print(leftSet - rightSet)
print(leftSet.difference(rightSet))
