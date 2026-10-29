def solve_15_1_naive(a):
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                return True
    return False

def solve_15_1_optimal(a):
    return len(a) != len(set(a))