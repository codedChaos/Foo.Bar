from fractions import Fraction as fract

def solution(pegs):
    print("solution_final -> pegs: ", pegs)
    lenPegs = len(pegs)
    if (lenPegs < 2):
        return [-1, -1]

    isEven = True if (lenPegs % 2 == 0) else False
    x = (- pegs[0] + pegs[lenPegs -1]) if isEven else (- pegs[0] - pegs[lenPegs - 1])

    if (lenPegs > 2):
        for i in range(1, lenPegs - 1):
            x += 2 * (-1)**(i+1) * pegs[i]

    G = []
    G.append(fract(2 * (float(x)/3 if isEven else x)).limit_denominator())         
    radius = G[0]
    
    if ((radius / 2 > (pegs[-1] - pegs[-2])) or (radius < 2)):
        return [-1, -1]
    
    for index in range(0, lenPegs - 1):
            dist = pegs[index + 1] - pegs[index]
            nextRadius = fract(dist - radius).limit_denominator()
            if (radius < 1 or nextRadius < 1):
                return [-1, -1]
            else:
                radius = nextRadius
                G.append(radius)

    return [G[0].numerator, G[0].denominator]

def solution2(pegs):
    print("solution2 -> pegs: ", pegs)
    lenPegs = len(pegs)
    if (lenPegs < 2):
        return [-1, -1]
    
    isEven = True if (lenPegs % 2 == 0) else False
    x = (- pegs[0] + pegs[lenPegs -1]) if isEven else (- pegs[0] - pegs[lenPegs - 1])

    if (lenPegs > 2):
        for i in range(1, lenPegs - 1):
            x += 2 * (-1)**(i+1) * pegs[i]

    G = []
    G.append(fract(2 * (float(x)/3 if isEven else x)).limit_denominator())
             
    radius = G[0]
    for index in range(0, lenPegs - 2):
            dist = pegs[index + 1] - pegs[index]
            nextRadius = dist - radius
            if (radius < 1 or nextRadius < 1):
                return [-1, -1]
            else:
                radius = nextRadius

    return [G[0].numerator, G[0].denominator]

def solution1(pegs):
    print("solution1 -> pegs: ", pegs)
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
        if ((prevRadius < 1) or (prevRadius > (w - 1))):
            return [-1, -1]

    return [int(a), int(b)]



from random import sample

assert((solution([4, 30, 50])) == [12, 1])
print(solution([1, 11]))
print(solution([4.5, 30.5, 50.5]))
print(solution([10, 50.77, 70, 90.5, 115, 150]))
print(solution([4, 9, 17, 31, 40]))
print(solution([4, 30, 50]))
assert((solution1([4, 30, 50])) == [12, 1])
print(solution1([1, 11]))
print(solution1([4.5, 30.5, 50.5]))
print(solution1([10, 50.77, 70, 90.5, 115, 150]))
print(solution1([4, 9, 17, 31, 40]))
print(solution1([4, 30, 50]))
assert((solution2([4, 30, 50])) == [12, 1])
print(solution2([1, 11]))
print(solution2([4.5, 30.5, 50.5]))
print(solution2([10, 50.77, 70, 90.5, 115, 150]))
print(solution2([4, 9, 17, 31, 40]))
print(solution2([4, 30, 50]))

for i in range(1, 150):
    a = sample([x for x in range(1, 10000)], k=(sample([x for x in range(2, 21)], k=1)[0]))
    a.sort()
    print(solution(a))
    print(solution1(a))
    print(solution2(a))

    
    
    
