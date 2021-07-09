# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class CustomZeroDivisionError(Exception):
    def __init__(self):
        self.txt = "this is not infinitesimal calculus, you can't devide by zero"
    def __str__(self):
        return self.txt

def custom_devide(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        print("Hello")
        raise CustomZeroDivisionError()



while True:
    number_1 = input('enter number1 for exit press enter: \n')
    number_2 = input('enter number2 for exit press enter: \n')
    if number_1 == '' or number_2 == '':
        print("Good Bye")
        break
    else:
        if number_1.isnumeric() and number_2.isnumeric():
            try:
                print(number_1, number_2, custom_devide(int(number_1), int(number_2)))
            except Exception as err:
                print(err)
        else:
            print("enter only numbers")
