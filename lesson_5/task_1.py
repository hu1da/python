# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("txt_files/task1.txt", "w") as in_f:
    while True:
        line = input("enter new line: ")
        if '' == line:
            break
        in_f.writelines([line, '\n'])
with open("txt_files/task1.txt", "r") as out_f:
    content = out_f.read()
    print(content)
