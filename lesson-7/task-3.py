# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

class Cell:
    def __init__(self, count):
        self.__count = count

    def __add__(self, other):
        return self.__count + other.__count

    def __sub__(self, other):
        res = self.__count - other.__count
        return res if res > 0 else 'invalid action'

    def __mul__(self, other):
        return self.__count * other.__count

    def __truediv__(self, other):
        return round(self.__count / other.__count)

    def make_order(self, row):
        res = ''
        base = self.__count // row
        rest = self.__count % row
        for i in range(base):
            for j in range(row) :
                res +='*'
            res+='\n'
        for j in range(rest):
            pass
            res += '*'
        return res


cell_1 = Cell(4)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(3))
print('---------')
print(cell_1.make_order(6))

