# Partition Generator Function
#from __future__ import print_function


def partition_generator():
    n = 2
    part_max = 200
    
    F = [0] * (part_max + 1)
    F[0], F[1] = 1, 1

    for n in range(2, part_max + 1, 1):
        for k in range(part_max, n - 1, -1):
            F[k] = F[k] + F[k-n]

    return [x - 1 for x in F]

part_cache = partition_generator()

def solution(n):
    if n >= 3 and n <= 200:
        return part_cache[n]

print(solution(200))
#for i in range(-1, 250):
#    print(solution(i))
#for i in part_cache:
#    print(i, end = " ")
