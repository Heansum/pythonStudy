condition = range(1, 11)

add = 0
for i in condition:
    add = add + i

print(add)

forward = 2

for backward in range(1,10):
    result = forward * backward
    print("{} * {} = {}".format(forward, backward, forward * backward))
