class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __str__(self):
        return f"Результат: {self.number * '*'}"

    def __add__(self, other):
        print('Сумма равна: ')
        return Cell(self.number + other.number)

    def __sub__(self, other):
        print('Разница равна: ')
        return self.number - other.number if (self.number - other.number) > 0 else print('Невозможно')

    def __mul__(self, other):
        print('Произведение равно: ')
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        print('Деление равно: ')
        return Cell(self.number // other.number)

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.number / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.number % cells_in_row)}'
        return row

cell1 = Cell(9)
cell2 = Cell(10)
print(cell1)
print(cell2)
print(cell1 + cell2)
print(cell2 - cell1)

