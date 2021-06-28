# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.


from itertools import count, cycle
from random import randint
from time import sleep

class TrafficLight:
    __colors = ['red', 'yellow', 'green']

    color = None

    def running(self, number):
        for idx, el in enumerate(cycle(self.__colors)):
            if idx > number:
                break
            sleep(randint(1, 3))
            self.__colors = el
            print(self.__colors)


traffic_lights = TrafficLight()
traffic_lights.running(50)
