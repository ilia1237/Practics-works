def solve_15_2_naive(a, b):
    return [x for x in a if x in b]

def solve_15_2_optimal(a, b):
    bset = set(b)
    return [x for x in a if x in bset]