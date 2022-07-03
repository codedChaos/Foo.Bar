def solution(n):
    if n < 3:
        return 0
    memoirs = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    return bricks(1, n, memoirs) - 1

def bricks(L, H, memoirs):
    if memoirs[L][H] != 0:
        return memoirs[L][H]
    if H == L:
        return 1
    if H < L:
        return 0

    memoirs[L][H] = (bricks(L + 1, H - L, memoirs)) + (bricks(L + 1, H, memoirs))
 
    return memoirs[L][H]

solution(200)
