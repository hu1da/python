# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
# test
print(reduce(lambda aggr, next: aggr * next, range(1, 5+1)))


print(reduce(lambda aggr, next: aggr * next, range(100, 1000+1)))