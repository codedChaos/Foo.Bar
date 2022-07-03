part = {}

def partit(N=10):
    global part

    for i in range(1, N + 1):
        part[i] = [(j, i - j) for j in range(1, i + 1) if j < i - j]

    for i in range(1, N + 1):
        temp = []
        for up, down in part[i]:
            p2 = [(up, (u, d)) for u, d in part[down] if u > up]
            temp.extend(p2)
        part[i].extend(temp)

    return {i:len(part[i])+1 for i in part}
