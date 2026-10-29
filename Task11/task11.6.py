def custom_sort(arr, reverse=False, key=None):
    a = arr.copy()
    for i in range(1, len(a)):
        val = a[i]
        val_key = key(val) if key else val
        j = i - 1
        while j >= 0:
            curr_key = key(a[j]) if key else a[j]
            condition = (curr_key > val_key) if not reverse else (curr_key < val_key)
            if condition:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = val
    return a

data_neg = [-5, 2, -1, 3]
sorted_abs = custom_sort(data_neg, key=abs)
print("За модулем:", sorted_abs)