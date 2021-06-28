# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print(f"turn {direction}")

    def show_speed(self):
        print(f"speed: {self.speed}")

    def to_string(self):
        return f"name: {self.name}, color: {self.color}, speed: {self.speed},  {'is a police car' if self.is_police else ''}"


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print("you exceeded the speed")
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print("you exceeded the speed")
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


# TownCar, SportCar, WorkCar, PoliceCar
town_car = TownCar(40, 'red', 'shkoda')
sport_car = SportCar(140, 'pink', 'bmw')
work_car = WorkCar(80, 'white', 'isuzu')
police_car = TownCar(200, 'blue', 'toyota')

print(town_car.to_string())
print(sport_car.to_string())
print(work_car.to_string())
print(police_car.to_string())

town_car.go()
town_car.show_speed()
town_car.turn('left')
town_car.stop()

work_car.go()
work_car.show_speed()
work_car.turn('right')
work_car.stop()

police_car.go()
police_car.show_speed()
police_car.turn('left')
police_car.stop()
