def solve_15_4_naive(a):
    return {x: a.count(x) for x in a}

def solve_15_4_optimal(a):
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    return counts