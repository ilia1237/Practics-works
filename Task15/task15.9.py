def solve_15_9_naive(a, k):
    a_copy = list(a)
    result = []
    for _ in range(k):
        val = max(a_copy)
        result.append(val)
        a_copy.remove(val)
    return result

def solve_15_9_optimal(a, k):
    return heapq.nlargest(k, a)