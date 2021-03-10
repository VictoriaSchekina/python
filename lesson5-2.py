#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
#выполнить подсчет количества строк, количества слов в каждой строке.

with open("textfile.txt", "r", encoding="utf-8") as f: #строчки вводим в новый файл в 1 задаче
    my_str = f.readlines()
    for index, val in enumerate(my_str, 1):
        words = len(val.split())
        print(f'Строка {index} содержит {words} слов')
