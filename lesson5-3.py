#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("salary.txt", "r", encoding="utf-8") as f:
    salary_list = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя зарплата = {round(sum(salary_list.values()) / len(salary_list), 3)}\n' f'Больше 20000 получают {[i[0] for e in salary_list.items() if i[1] < 20000]}')
