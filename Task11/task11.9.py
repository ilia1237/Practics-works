def binary_search_recursive(arr, target, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = lo + (hi - lo) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, hi)
    else:
        return binary_search_recursive(arr, target, lo, mid - 1)

# Перевірка на всіх елементах і відсутніх значеннях
sorted_arr = [1, 3, 5, 7, 9, 11]
test_vals = [1, 5, 11, 4, 15]
for val in test_vals:
    res_iter, _ = binary_search_iterative(sorted_arr, val)
    res_rec = binary_search_recursive(sorted_arr, val)
    print(f"Значення {val}: ітеративно = {res_iter}, рекурсивно = {res_rec} (збігаються: {res_iter == res_rec})")