class Student:
    """Студент із прізвищем, групою та списком оцінок."""
    
    def __init__(self, surname: str, group: str):
        self.surname = surname
        self.group = group
        self.grades: list[int] = []

    def add_grade(self, score: int):
        """Додає оцінку з перевіркою діапазону 0..100."""
        if not (0 <= score <= 100):
            raise ValueError("Оцінка має бути в межах від 0 до 100")
        self.grades.append(score)

    def average(self) -> float:
        """Обчислює середній бал студента."""
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def best(self) -> int:
        """Повертає найвищу оцінку студента."""
        if not self.grades:
            raise ValueError("Список оцінок порожній")
        return max(self.grades)

    def ects(self) -> str:
        """Визначає оцінку за шкалою ECTS."""
        avg = self.average()
        if avg >= 90: return "A"
        if avg >= 82: return "B"
        if avg >= 75: return "C"
        if avg >= 67: return "D"
        if avg >= 60: return "E"
        return "F"

    def __len__(self) -> int:
        return len(self.grades)

    def __str__(self) -> str:
        return f"Студент {self.surname} ({self.group}), сер. бал: {self.average():.2f}"

    def __repr__(self) -> str:
        return f"Student(surname='{self.surname}', group='{self.group}')"

if __name__ == "__main__":
    s = Student("Коваль", "КН-21")
    s.add_grade(85)
    s.add_grade(95)
    assert len(s) == 2
    assert s.best() == 95
    assert s.average() == 90.0