# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
from functools import reduce

CONST_PATH = "txt_files/task5.txt"

with open(CONST_PATH, "w") as in_f:
    while True:
        line = input("enter new line: ")
        if '' == line:
            break
        in_f.writelines([line, '\n'])
with open(CONST_PATH, "r") as out_f:
    content = out_f.read()
numbers = content.split()
total = reduce(lambda x, y: float(x) + float(y), numbers, 0)
print(f"total sum: {total}")
