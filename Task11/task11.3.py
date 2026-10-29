def bubble_sort(arr):
    a = arr.copy()
    comparisons = 0
    swaps = 0
    passes = 0
    n = len(a)
    for i in range(n - 1):
        passes += 1
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return a, comparisons, swaps, passes

res, comp, sw, passes = bubble_sort(test_sets["B"])
print(f"Набір B: проходів = {passes}, порівнянь = {comp}, обмінів = {sw}")