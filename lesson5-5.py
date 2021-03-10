#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    try:
        with open("textfile5.txt", "w", encoding="utf-8") as f:
            my_str = input('Введите цифры через пробел \n')
            f.writelines(my_str)
            my_numb = my_str.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()
