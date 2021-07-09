# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class CustomComplexNumber():
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __str__(self):
        return f"{self.__a} + {self.__b}i"

    def __add__(self, other):
        return CustomComplexNumber(self.__a + other.__a, self.__b + other.__b)

    def __mul__(self, other):
        return CustomComplexNumber(self.__a * other.__a - self.__b * other.__b,
                                   self.__a * other.__a + self.__b * other.__b)


complex_1 = CustomComplexNumber(2, 3)
complex_2 = CustomComplexNumber(4, 5)

print(f"number one: {complex_1}, number two: {complex_2}, sum: {complex_1 + complex_2}, multiplication: {complex_1 * complex_2}")
