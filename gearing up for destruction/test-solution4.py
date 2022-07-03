# solution fails 4-5 test cases
# suspect it doesn't handle fractional radii well enough

def solution1(pegs):
    lenP = len(pegs)

    if ((not pegs) or lenP == 1):
        return [-1, -1]
    
    a = pegs[0]
    gradient = -1
    for peg in pegs:
        a += 2 * peg * gradient
        gradient *= -1
    a += pegs[lenP - 1] * gradient
    a *= 2
    b = 3 if (lenP % 2 == 0) else 1

    if ((b == 3) and (a % b == 0)):
        a /= b
        b = 1

    prevRadius = float(float(a) / float(b))
    for i in range(0, lenP - 2):
        w = int(pegs[i+1] - pegs[i])
        if ((prevRadius < 0) or (prevRadius > (w - 1))):
            return [-1, -1]

    return [a, b]

print(solution([4, 9, 17, 31, 40]))
print(solution([1, 11]))
    
