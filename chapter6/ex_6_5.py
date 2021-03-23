forward = 2

for backward in range(1,10):
    result = forward * backward
    print("%d * %d = %d" % (forward, backward, result))


for forward in range(2,10):
    for backward in range(1,10):
        result = forward * backward
        print("%d * %d = %d" % (forward, backward, result))
    print("\n")

