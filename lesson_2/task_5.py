# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

_list = [7, 5, 3, 3, 2]
print(_list)
_list.append(float('-inf'))
while True:
    number = input("enter a number, to stop print 'stop': ")
    if number == 'stop':
        break
    number = int(number)
    length = len(_list)
    current = 0
    while current < length:
        if number >= _list[current]:
            _list.insert(current, number)
            break
        current += 1
    print('tmp result: ', _list)
_list.pop()
print('final result: ', _list)
print('end')
