def linear_search(arr, target):
    comparisons = 0
    for i, x in enumerate(arr):
        comparisons += 1
        if x == target:
            return i, comparisons
    return -1, comparisons

print("A, 9 ->", linear_search(A, 9))      # індекс 2 (3 порівняння)
print("A, 100 ->", linear_search(A, 100))  # -1 (6 порівнянь)