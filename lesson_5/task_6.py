# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

CONST_PATH = "txt_files/text_6.txt"
data = {}

with open(CONST_PATH) as out_f:
    for line in out_f:
        line_data = line.split()
        total = 0
        for idx in range(1, len(line_data)):
            num_str = line_data[idx].split("(")[0]
            try:
                num = int(num_str)
                total += num
            except:
                pass
        data[line_data[0]] = total
print(data)
