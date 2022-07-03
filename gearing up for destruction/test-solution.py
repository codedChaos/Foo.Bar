def solution(pegs):
    lP = len(pegs)
    if ((not pegs) or lP == 1):
        return [-1, -1]
    
    D = [pegs[p+1] - pegs[p] for p in range(lP-1)]
    G = [0]

    for i in D:
        G[0] = i - G[0]

    x = G[0]
    lD = len(D)

    # failing tests # 3, 8
    
    if lD % 2 == 0:
        ret = [x * -2, 1]
    elif lD % 2 == 1:
        if x * 2 % 3 == 0:
            ret = [x * 2/3, 1]
        else:
            ret = [x * 2, 3]

    G[0] = ret
    
    if (G[0][0] % G[0][1] == 0):
        #print("reduce", G[0])
        G[0][0] /= G[0][1]
        G[0][1] = 1

    x = G[0][0]    
    if lD % 2 == 0:
        for i in D:
            x = i - x
            G.append([x, G[0][1]])
    elif lD % 2 == 1:
        x = x // 2
        G.append([x, G[0][1]])
    
    if any([True for x in G if x[0] < 1]):
        return[-1, -1]
    else:
        return G[0]

#print(solution([4, 9, 17, 31, 40]))
#print(solution([4, 17, 50]))
#print(solution([1, 11]))
#print(solution([110, 13]))
#print(solution([150, 500, 750, 1000]))
#print(solution([250, 630, 752, 1000, 1500, 2200, 4500, 7800, 10000]))
#print(solution([4.5, 30.5, 50.5]))
#print(solution([10, 50.77, 70, 90.5, 115, 150]))
print(solution([2270, 4266, 5480, 6128, 6799, 7505, 8798, 9968]))
