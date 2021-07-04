# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, *args):
        if len(args) == 1:
            self.data = args[0]
        if len(args) > 1:
            numbers, step = args[0], args[1]
            self.data = []
            for idx in range(0, len(numbers), step):
                line = []
                for j in range(step):
                    if idx < len(numbers):
                        line.append(numbers[idx])
                        idx += 1
                    else:
                        line.append(0)
                self.data.append(line)


    def __str__(self):
        printable = ''
        for line in self.data:
            for number in line:
                printable += '  ' + str(number)
            printable += '\n'
        return printable

    def __add__(self, other):
        result = []
        col_count = max(len(self.data[0]), len(other.data[0]))
        row_count = max(len(self.data), len(other.data))
        for row in range(row_count):
            line = []
            for itemIdx in range(col_count):
                if row < len(self.data) and itemIdx < len(self.data[0]):
                    item_1 = self.data[row][itemIdx]
                else:
                    item_1 = 0
                if row < len(other.data) and itemIdx < len(other.data[0]):
                    item_2 = other.data[row][itemIdx]
                else:
                    item_2 = 0
                line.append(item_1 + item_2)
            result.append(line)
        return Matrix(result)


from random import randint

arr_1 = []
arr_2 = []

for idx in range(10):
    arr_1.append(randint(0, 9))
    arr_2.append(randint(0, 9))

matrix_1 = Matrix(arr_1, 5)
matrix_2 = Matrix(arr_2, 4)

print(matrix_1)
print(matrix_2)
merged = matrix_1 + matrix_2
print(merged)
