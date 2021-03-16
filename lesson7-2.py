# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте
# относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост
# (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.



class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def get_size_c(self):
        return self.width / 6.5 + 0.5

    def get_size_j(self):
        return self.height * 2 + 0.3


    # создаем свойство
    @property
    def get_size_full(self):
        return str(f'Площадь ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.size_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.size_c}'


class Jacket(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.size_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.size_j}'

coat = Coat(3, 5)
jacket = Jacket(3, 3)
print(coat)
print(jacket)
print(coat.get_size_full)
print(jacket.get_size_full)
print(jacket.get_size_c())
print(jacket.get_size_j())