def quick_sort_first_pivot(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # Невдалий вибір для відсортованих даних
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort_first_pivot(less) + equal + quick_sort_first_pivot(greater)

# Набір B [1, 2, 3, 4, 5] викликає найглибшу рекурсію O(n) та O(n^2) часу
print(quick_sort_first_pivot([1, 2, 3, 4, 5]))