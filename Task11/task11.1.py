def selection_sort(arr):
    a = arr.copy()
    comparisons = 0
    swaps = 0
    n = len(a)
    for i in range(n - 1):
        mi = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[mi]:
                mi = j
        if mi != i:
            a[i], a[mi] = a[mi], a[i]
            swaps += 1
    return a, comparisons, swaps

for name, data in test_sets.items():
    res, comp, sw = selection_sort(data)
    print(f"Набір {name}: порівнянь = {comp}, обмінів = {sw}")