def solve_15_6_naive(n):
    if n < 2:
        return n
    return solve_15_6_naive(n - 1) + solve_15_6_naive(n - 2)

def solve_15_6_optimal(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b