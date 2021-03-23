#Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен
# проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def extract(cls, date):
        my_date = []
        for i in date.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if  1 <= day <= 31:
            if 1 <= month <= 12:
                    return f'Дата верна'
            else:
                return f'Исправьте месяц'
        else:
            return f'Исправьте день'


    def __str__(self):
        return f'Текущая дата {Date.extract(self.date)}'


today = Date('11 - 2 - 2021')
print(today)
print(Date.valid(11, 1, 2021))
print(Date.valid(33, 1, 2021))
print(Date.valid(30, 13, 2021))

#только в задаче не прописано количество дней в месяце
#(например, что в феврале не может быть 30 дней),
#а также високосные года, в целях экономии времени,
#но при необходимости это можно сделать в валидности