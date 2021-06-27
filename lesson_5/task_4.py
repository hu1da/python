# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dictionary = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}
with open("txt_files/text_4.txt") as out_f:
    with open("txt_files/text_4_in.txt", "w") as in_f:
        for line in out_f:
            new_line = line.split()
            new_line[0] = dictionary[new_line[0].lower()]
            in_f.writelines([" ".join(new_line), '\n'])
with open("txt_files/text_4_in.txt", "r") as out_f:
    content = out_f.read()
    print(content)
