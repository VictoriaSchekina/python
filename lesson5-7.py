#7 Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).

import json

with open("textfile6_json.txt", "w", encoding="utf-8") as file1:
    with open("textfile6.txt", encoding="utf-8") as file2:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in file2}
        result = [profit, {"average_profit": round(sum([int(i) for i in profit.values() if int(i) > 0]) / len([int(i) for i in profit.values() if int(i) > 0]))}]
        json.dump(result, file1)
