students = [("Шевченко", 92), ("Коваль", 74), ("Бондар", 92), ("Ткач", 58)]
d_students = dict(students)

best_student = max(d_students, key=d_students.get)
worst_student = min(d_students, key=d_students.get)

print(
    f"Найкращий: {best_student} ({d_students[best_student]}), Найгірший:"
    f" {worst_student} ({d_students[worst_student]})"
)