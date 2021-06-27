# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

lineNumber = 0
with open("txt_files/text_7.txt") as out_f:
    for line in out_f:
        lineNumber += 1
        print(f"in {lineNumber} line: {len(line.split())} words")
print(f"number of lines: {lineNumber}")
