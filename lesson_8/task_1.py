# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных


class Date():
    __delimiter = '-'

    def __init__(self, s_date):
        __s_date = s_date

    @classmethod
    def str_to_date(cls, s_data):
        s_day, s_month, s_year = s_data.split(cls.__delimiter)
        return (int(s_day), int(s_month), int(s_year))

    @staticmethod
    def validate(tuple_date):
        error_msg = ''
        if tuple_date[2] < 1:
            error_msg += "a year should be positive number\n"
        if tuple_date[1] < 1 or tuple_date[1] > 12:
            error_msg += "a month should be betweeon 1-12\n"
        if tuple_date[0] < 1:
            error_msg += "a day should be positive number\n"
        elif [1, 3, 5, 7, 8, 10, 12].__contains__(tuple_date[1]) and tuple_date[0] > 31:
            error_msg += "for selected month day should be less then 31\n"
        elif [4, 6, 9, 11].__contains__(tuple_date[1]) and tuple_date[0] > 30:
            error_msg += "for selected month day should be less then 30\n"
        elif tuple_date[1] == 2 and ((tuple_date[0] > 29 and tuple_date[2] % 4 == 0) or tuple_date[0] > 29):
            error_msg += "too many days for February\n"
        if error_msg:
            raise Exception(tuple_date, error_msg)


data_1 = Date.str_to_date("31-07-1978")
print(data_1)

try:
    Date.validate(data_1)
except Exception as err:
    print(err)

data_1 = Date.str_to_date("32-07-1978")
print(data_1)

try:
    Date.validate(data_1)
except Exception as err:
    print(err)

data_1 = Date.str_to_date("31-06-1977")
print(data_1)

try:
    Date.validate(data_1)
except Exception as err:
    print(err)

data_1 = Date.str_to_date("31-02-2000")
print(data_1)

try:
    Date.validate(data_1)
except Exception as err:
    print(err)

data_1 = Date.str_to_date("31-02-1978")
print(data_1)

try:
    Date.validate(data_1)
except Exception as err:
    print(err)

data_1 = Date.str_to_date("29-02-2000")
print(data_1)

try:
    Date.validate(data_1)
except Exception as err:
    print(err)

data_1 = Date.str_to_date("28-02-2001")
print(data_1)

try:
    Date.validate(data_1)
except Exception as err:
    print(err)

