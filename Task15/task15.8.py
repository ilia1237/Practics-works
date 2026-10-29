def solve_15_8_naive(a, target):
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] == target:
                return (a[i], a[j])
    return None

def solve_15_8_optimal(a, target):
    seen = set()
    for x in a:
        diff = target - x
        if diff in seen:
            return (diff, x)
        seen.add(x)
    return None