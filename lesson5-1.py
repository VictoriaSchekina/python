#1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("textfile.txt", "w", encoding="utf-8") as f:
    while True:
        my_str = input('Введите фразу: ')
        if not my_str:
            break
        print(my_str, file=f)


