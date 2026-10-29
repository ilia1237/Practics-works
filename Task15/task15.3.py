def solve_15_3_naive(parts):
    s = ""
    for ch in parts:
        keep = s
        s = keep + ch
    return s

def solve_15_3_optimal(parts):
    return "".join(parts)