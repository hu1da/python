# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

step = int(input("Enter a list length: "))
list = []

while step > 0:
    number = int(input("Enter a number: "))
    list.append(number)
    step -= 1

print('source: ', list)

step = 2

length = len(list)
while step <= length:
    tmp = list[step-1]
    list[step - 1] = list[step - 2]
    list[step - 2] = tmp
    step+=2

print('target: ', list)
