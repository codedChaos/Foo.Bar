from distutils.version import LooseVersion

def solution(l):
    # sort list of major.minor.revision numbers given as strings
    l.sort(key=LooseVersion)
    return l

assert solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]) == \
       ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]

solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])

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
