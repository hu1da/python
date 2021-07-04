# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    name = ''
    consumption: -1

    def __init__(self, name, consumption):
        self.name = name
        self.__consumption = consumption

    def __str__(self):
        return f"name: {self.name}\n consumption: {self.__consumption}"


class Coat(Clothes):
    def __init__(self, V):
        self.consumption = V
        super().__init__('coat', self.consumption)

    @property
    def consumption(self):
        return self.__consumption

    @consumption.setter
    def consumption(self, V):
        self.__consumption = (V / 6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, H):
        self.consumption = H
        super().__init__('suit', self.consumption)

    @property
    def consumption(self):
        return self.__consumption

    @consumption.setter
    def consumption(self, H):
        self.__consumption = (2 * H + 0.3)


coat = Coat(13)
print(coat)

suit = Suit(10)
print(suit)

