class Tech:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'


    def reception(self):
        try:
            unit = input(f'Введите модель ')
            unit_p = int(input(f'Введите цену '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель': unit, 'Цена': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f' ')
        if q == 'Q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Tech.reception(self)


class Printer(Tech):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Tech):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Xerox(Tech):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('HP', 3000, 2, 10)
unit_2 = Scanner('HP', 4000, 3, 20)
unit_3 = Xerox('Xerox', 3000, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())