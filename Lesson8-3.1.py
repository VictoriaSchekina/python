#3. Создайте собственный класс-исключение, который должен проверять содержимое списка
# на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class Numbers:
    def __init__(self, *args):
        self.my_list = []

    def my_numbers(self):
        while True:
            try:
                num = int(input('Введите значения и нажимайте однократно Enter для продолжения и 2 раза для того чтобы закончить - '))
                self.my_list.append(num)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print('Недопустимые значения')
                enter = input('Продолжить ввод? да или нет')

                if enter == 'да':
                    print(try_except.my_numbers())
                elif enter == 'нет':
                    return f'Конец'
                else:
                    return f'Конец'


try_except = Numbers(1)
print(try_except.my_numbers())