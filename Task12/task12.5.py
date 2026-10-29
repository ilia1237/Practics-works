sub = {1, 5}
b_set = set(b)

is_subset = sub.issubset(b_set)  # або sub <= b_set
is_disjoint = sub.isdisjoint({7, 11})  # чи не перетинаються

print("Чи є підмножиною:", is_subset)
print("Чи не перетинаються:", is_disjoint)