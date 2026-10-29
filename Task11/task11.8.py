def binary_search_iterative(arr, target):
    lo, hi = 0, len(arr) - 1
    mids = []
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        mids.append(mid)
        if arr[mid] == target:
            return mid, mids
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, mids

idx, mids = binary_search_iterative([1, 3, 5, 7, 9, 11], 9)
print(f"Індекс: {idx}, mid: {mids}")