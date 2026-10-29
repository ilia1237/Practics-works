class BankAccount:
    """Банківський рахунок із власником та захищеним балансом."""
    
    def __init__(self, owner: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")
        self.owner = owner
        self._balance = initial_balance
        self._history: list[str] = [f"Створено рахунок з балансом {initial_balance}"]

    @property
    def balance(self) -> float:
        """Поточний баланс рахунку (тільки для читання)."""
        return self._balance

    def deposit(self, amount: float):
        """Поповнює рахунок на вказану суму."""
        if amount <= 0:
            raise ValueError("Сума поповнення має бути додатною")
        self._balance += amount
        self._history.append(f"Депозит: +{amount}")

    def withdraw(self, amount: float):
        """Знімає кошти з перевіркою на від'ємний баланс."""
        if amount <= 0:
            raise ValueError("Сума зняття має бути додатною")
        if amount > self._balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self._balance -= amount
        self._history.append(f"Зняття: -{amount}")

    def history(self) -> list[str]:
        """Повертає історію всіх операцій."""
        return self._history.copy()

    def __str__(self) -> str:
        return f"Рахунок власника {self.owner}, баланс: {self._balance}"

    def __repr__(self) -> str:
        return f"BankAccount(owner='{self.owner}', balance={self._balance})"

if __name__ == "__main__":
    acc = BankAccount("Іван", 100.0)
    acc.deposit(50.0)
    acc.withdraw(30.0)
    assert acc.balance == 120.0
    assert len(acc.history()) == 3
    try:
        acc.withdraw(500.0)
    except ValueError:
        assert True