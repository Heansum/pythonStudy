leftSet = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
rightSet = set([2, 4, 6, 8, 10, 12, 14, 16, 18])

print(leftSet & rightSet)
print(leftSet.intersection((rightSet)))     # 교집합

leftSet = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
rightSet = set([2, 4, 6, 8, 10, 12, 14, 16, 18])

print(leftSet | rightSet)
print(leftSet.union(rightSet))              # 합집합

leftSet = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
rightSet = set([2, 4, 6, 8, 10, 12, 14, 16, 18])

print(leftSet - rightSet)
print(leftSet.difference(rightSet))

