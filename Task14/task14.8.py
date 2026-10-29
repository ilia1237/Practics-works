class Matrix:
    """Матриця на базі списку списків."""
    
    def __init__(self, data: list[list[float]]):
        if not data or not data[0]:
            raise ValueError("Матриця не може бути порожньою")
        row_len = len(data[0])
        for row in data:
            if len(row) != row_len:
                raise ValueError("Усі рядки матриці повинні мати однакову довжину")
        self.data = [row.copy() for row in data]
        self.rows = len(data)
        self.cols = row_len

    def __getitem__(self, index):
        return self.data[index]

    def transpose(self):
        """Повертає транспоновану матрицю."""
        transposed_data = [[self.data[r][c] for r in range(self.rows)] for c in range(self.cols)]
        return Matrix(transposed_data)

    def __add__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Розміри матриць мають збігатися для додавання")
        new_data = [[self.data[r][c] + other.data[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return Matrix(new_data)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_data = [[self.data[r][c] * other for c in range(self.cols)] for r in range(self.rows)]
            return Matrix(new_data)
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Кількість стовпців першої матриці має дорівнювати кількості рядків другої")
            new_data = [
                [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)]
                for i in range(self.rows)
            ]
            return Matrix(new_data)
        return NotImplemented

    def __str__(self) -> str:
        return "\n".join([" ".join(map(str, row)) for row in self.data])

    def __repr__(self) -> str:
        return f"Matrix({self.data})"

if __name__ == "__main__":
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    m3 = m1 + m2
    assert m3[0] == [6, 8]
    assert m3[1] == [10, 12]
    assert m1.transpose()[0] == [1, 3]