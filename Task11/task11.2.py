def insertion_sort(arr):
    a = arr.copy()
    comparisons = 0
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key
    return a, comparisons, shifts

for name in ["A", "B", "C"]:
    _, comp, shifts = insertion_sort(test_sets[name])
    print(f"Набір {name}: порівнянь = {comp}, зсувів = {shifts}")