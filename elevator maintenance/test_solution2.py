def solution(l):
    sorted_list = sorted([[int(y) for y in x.split('.')] for x in l])
    final = []
    for a in sorted_list:
        a = '.'.join(str(z) for z in a)
        final.append(a)
    return final


print(solution([
        '1.1.2', '1.0', '1.3.3', '1.0.12', '1.0.2', '0.0.1', '0', \
        '0.11.0', '0.1', '9.0.1', '1.1.0', '0.1.0', '1.1', '1', '1.0.0'
        ]))

print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
print(solution(["0.0.0", "0.0", '0.0.9', "0.1.0", "0.1.1", "0.12", "0.0.11"]))

import random

def test_solution():
    test_list = []
    while len(test_list) < random.randrange(1, 101):
            n = random.randrange(1, 3)
            a = list([random.randrange(0, 15) for _ in range(n+1)])
            test_list.append(a)
    test_list = ['.'.join(str(x) for x in a) for a in test_list]
    print(test_list)
    return test_list

print(solution(test_solution()))
