# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

lineNumber = 0
CONST_SALARY = 20000
employees = []
with open("txt_files/text_3.txt") as out_f:
    for line in out_f:
        name, salary = line.split()
        if float(salary) >= CONST_SALARY:
            employees.append(name)

print(employees)
