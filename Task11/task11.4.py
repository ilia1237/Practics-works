def merge_sort_tracked(arr):
    max_depth = 0
    
    def sort(sub_a, depth):
        nonlocal max_depth
        if depth > max_depth:
            max_depth = depth
        if len(sub_a) <= 1:
            return sub_a
        mid = len(sub_a) // 2
        left = sort(sub_a[:mid], depth + 1)
        right = sort(sub_a[mid:], depth + 1)
        return merge(left, right)

    def merge(x, y):
        res = []
        i = j = 0
        while i < len(x) and j < len(y):
            if x[i] <= y[j]:
                res.append(x[i]); i += 1
            else:
                res.append(y[j]); j += 1
        res.extend(x[i:])
        res.extend(y[j:])
        return res

    sorted_arr = sort(arr, 1)
    return sorted_arr, max_depth

_, depth = merge_sort_tracked(A)
print(f"Глибина рекурсії для набору A: {depth}")