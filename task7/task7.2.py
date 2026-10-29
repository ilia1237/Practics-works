s = "алгоритм і програма"
vowels = "аеєиіїоуюя"
consonants = "бвгґджзклмнпрстфхцчшщ"

v_count = sum(1 for c in s.lower() if c in vowels)
c_count = sum(1 for c in s.lower() if c in consonants)
other_count = len(s) - v_count - c_count

print(f"голосних {v_count}, приголосних {c_count}, інших {other_count}")