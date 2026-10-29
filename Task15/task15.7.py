def solve_15_7_naive(n):
    a = []
    for x in range(n):
        a.insert(0, x)
    return a

def solve_15_7_optimal(n):
    d = collections.deque()
    for x in range(n):
        d.appendleft(x)
    return list(d)