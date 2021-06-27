# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

CONST_PATH = "txt_files/text_7.txt"
data = {}

with open(CONST_PATH) as out_f:
    for line in out_f:
        name, type, revenue, expenses = line.split()
        total = 0
        try:
            profit = float(revenue) - float(expenses)
            data[name] = profit
            if profit > 0:
                total += profit
        except:
            pass
list = [data, {"average_profit":total / len(data)}]
print(list)

with open("txt_files/text_7.json", "w") as in_f:
    json.dump(list, in_f, ensure_ascii=False)
