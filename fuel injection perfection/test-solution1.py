from timeit import timeit


def solution(n):
    print "solution(%d)" % n
    key = n = long(n)
    ops = 0

    while (n != 1):
        if (n & 1 == 0):
            n >>= 1
        elif ((n == 3) or ((n + 1) & n) > ((n - 1) & (n - 2))):
            n -= 1
        else:
            n += 1
        
        ops += 1
        solution(n)

    print "%d: %d" % (key, ops)
    return ops


for i in range(1, 100, -1):
    solution(i)
