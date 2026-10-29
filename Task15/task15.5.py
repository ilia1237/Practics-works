def solve_15_5_naive(a, queries):
    return [x in a for x in queries]

def solve_15_5_optimal(a, queries):
    aset = set(a)
    return [x in aset for x in queries]