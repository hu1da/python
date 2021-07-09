# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.


class CustomIsNotNumberError(Exception):
    def __init__(self):
        self.txt = "it's not a number, silly, be attentive."

    def __str__(self):
        return self.txt

arr = []

while True:
    num = input('enter number for exit press enter: \n')
    if num == 'stop':
        break
    else:
        try:
            if num.isnumeric():
                arr.append(float(num))
            else:
                raise CustomIsNotNumberError
        except CustomIsNotNumberError as err:
            print(err)
print(arr)