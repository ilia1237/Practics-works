from abc import ABC, abstractmethod

class Person(ABC):
    """Абстрактний клас Особа."""
    
    def __init__(self, surname: str, age: int):
        if age < 0:
            raise ValueError("Вік не може бути від'ємним")
        self.surname = surname
        self.age = age

    @abstractmethod
    def info(self) -> str:
        """Повертає інформаційну строку про особу."""
        pass

class StudentPerson(Person):
    def __init__(self, surname: str, age: int, group: str, grades: list[int]):
        super().__init__(surname, age)
        self.group = group
        self.grades = grades

    def info(self) -> str:
        return f"Студент: {self.surname}, вік {self.age}, група {self.group}"

class TeacherPerson(Person):
    def __init__(self, surname: str, age: int, subject: str, experience: int):
        super().__init__(surname, age)
        self.subject = subject
        self.experience = experience

    def info(self) -> str:
        return f"Викладач: {self.surname}, вік {self.age}, предмет {self.subject}, стаж {self.experience}р."

class University:
    """Університет, що містить список людей."""
    
    def __init__(self, name: str):
        self.name = name
        self.people: list[Person] = []

    def add(self, person: Person):
        """Додає особу до університету."""
        self.people.append(person)

    def students(self) -> list[StudentPerson]:
        """Повертає список лише студентів."""
        return [p for p in self.people if isinstance(p, StudentPerson)]

    def teachers(self) -> list[TeacherPerson]:
        """Повертає список лише викладачів."""
        return [p for p in self.people if isinstance(p, TeacherPerson)]

    def __len__(self) -> int:
        return len(self.people)

if __name__ == "__main__":
    uni = University("НУХ")
    s = StudentPerson("Коваль", 18, "КН-21", [85, 90])
    t = TeacherPerson("Шевченко", 45, "Алгоритми", 20)
    uni.add(s)
    uni.add(t)

    assert len(uni) == 2
    assert len(uni.students()) == 1
    assert len(uni.teachers()) == 1
    assert isinstance(s, Person)