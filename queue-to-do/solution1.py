# Queue-to-Do XOR Problem
def test_solution(s, l):
    chkSum = 0
    for x in range(l, 0, -1):
        #print "solution(%d, %d): -> for %d in range(%d, 0, -1)" % (s, l, x, l)
        chkSum ^= (test_get_xor(s + x-1) ^ test_get_xor(s-1))
        s += l
        print "chkSum: %d and s: %d" % (chkSum, s)
    return chkSum

def test_get_xor(x):
    print "get_xor(%d): ->" % (x)
    result = [x, 1, x + 1, 0]
    print "get_xor -> %d" % (result[x%4])
    return result[x % 4]        

def solution(s, l):
    chkSum = 0
    for L in range(l, 0, -1):
        chkSum = chkSum ^ (get_xor(s + L-1) ^ get_xor(s-1))
        s = s + l
    return chkSum

def get_xor(x):
    result = [x, 1, x + 1, 0]
    print result[x % 4]
    return result[x % 4]



print(test_solution(10, 4))


