class Time:
    """Час (години, хвилини, секунди)."""
    
    def __init__(self, hours: int, minutes: int, seconds: int):
        if hours < 0:
            raise ValueError("Години не можуть бути від'ємними")
        if not (0 <= minutes < 60):
            raise ValueError("Хвилини мають бути в межах від 0 до 59")
        if not (0 <= seconds < 60):
            raise ValueError("Секунди мають бути в межах від 0 до 59")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_seconds(self) -> int:
        """Конвертує час у загальну кількість секунд від початку доби."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds: int):
        """Створює об'єкт Time із загальної кількості секунд."""
        total_seconds %= 86400
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        return cls(h, m, s)

    def __add__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return Time.from_seconds(self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return Time.from_seconds(self.to_seconds() - other.to_seconds())

    def __lt__(self, other) -> bool:
        if not isinstance(other, Time):
            return NotImplemented
        return self.to_seconds() < other.to_seconds()

    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __repr__(self) -> str:
        return f"Time({self.hours}, {self.minutes}, {self.seconds})"

if __name__ == "__main__":
    t1 = Time(1, 30, 0)
    t2 = Time(0, 45, 30)
    assert (t1 + t2).to_seconds() == 8130
    assert t2 < t1
    assert str(Time(9, 5, 2)) == "09:05:02"