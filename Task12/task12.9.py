store1 = {"хліб": 25, "молоко": 30}
store2 = {"хліб": 23, "сир": 90}

s1_keys, s2_keys = set(store1.keys()), set(store2.keys())
common_keys = s1_keys & s2_keys
only_1 = s1_keys - s2_keys
only_2 = s2_keys - s1_keys

# Знаходимо найдешевшу ціну для кожного спільного товару
cheapest_common = {k: min(store1[k], store2[k]) for k in common_keys}

print("Спільні товари (найдешевше):", cheapest_common)
print("Лише в 1 магазині:", only_1)
print("Лише в 2 магазині:", only_2)