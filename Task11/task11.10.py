import time
import random

data = [random.randint(-10000, 10000) for _ in range(2000)]

def benchmark(sort_func, data):
    start = time.perf_counter()
    sort_func(data)
    end = time.perf_counter()
    return round((end - start) * 1000, 4) # у мілісекундах

t_selection = benchmark(lambda d: selection_sort(d)[0], data)
t_insertion = benchmark(lambda d: insertion_sort(d)[0], data)
t_bubble = benchmark(lambda d: bubble_sort(d)[0], data)
t_merge = benchmark(lambda d: merge_sort_tracked(data)[0], data)
t_builtin = benchmark(lambda d: sorted(d), data)