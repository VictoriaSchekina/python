# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

a = [31, 22], [37, 43], [51, 86]
b = [1, 2], [3, 4], [5, 6]

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        c = []
        for i in range(len(self.matrix)):
            c.append([])
            for j in range(len(self.matrix[0])):
                c[i].append(self.matrix[i][j] + other.matrix[i][j])
        return '\n'.join(map(str, c))


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)

print(f"Matrix 1:\n{matrix_1}")
print("*" * 20)
print(f"Matrix 2:\n{matrix_2}")
print("*" * 20)
print(f"matrix_1 + matrix_2:\n{matrix_1 + matrix_2}")
