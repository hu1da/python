# 4. Начните работу над проектом «Склад оргтехники».
#       Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
#       Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#       В базовом классе определить параметры, общие для приведенных типов.
#       В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием.
#       Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
#       Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
#       например словарь.
# 6. Продолжить работу над вторым заданием.
#       Реализуйте механизм валидации вводимых пользователем данных.
#       Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class Storage:
    def __init__(self):
        self.__products = []

    def __str__(self):
        res = ''
        for item in self.__products:
            res += f"[{item}]\n"
        return res

    def add_product(self, product):
        if product.validate():
            self.__products.append(product)
        else:
            raise Exception(f"invalid data for {type(product).__name__}")

    def move_product_to_department(self, serial_number, department):
        item = any(product.serial_number == serial_number for product in self.__products)
        if item:
            item.department = department


from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    def __init__(self, name, serial_number, manufacturer):
        self.name = name
        self.serial_number = serial_number,
        self.manufacturer = manufacturer

    def __str__(self):
        return f"name: {self.name}, serial number: {self.serial_number}, manufacturer: {self.manufacturer}"

    @abstractmethod
    def validate(self):
        pass


class Computer(OfficeEquipment):
    def __init__(self, name, serial_number, manufacturer, RAM, CPU):
        super().__init__(name, serial_number, manufacturer)
        self.RAM = RAM
        self.CPU = CPU

    def __str__(self):
        return f"{super().__str__()}, RAM: {self.RAM}, CPU: {self.CPU}"

    def validate(self):
        return self.RAM.isnumeric() and self.CPU.isnumeric()


class Scaner(OfficeEquipment):
    def __init__(self, name, serial_number, manufacturer, resolution, color_depth):
        super().__init__(name, serial_number, manufacturer)
        self.resolution = resolution
        self.color_depth = color_depth

    def __str__(self):
        return f"{super().__str__()}, resolution: {self.resolution}, color depth: {self.color_depth}"

    def validate(self):
        return self.resolution.isnumeric() and self.color_depth.isnumeric()


class Shreder(OfficeEquipment):
    def __init__(self, name, serial_number, manufacturer, speed, capacity):
        super().__init__(name, serial_number, manufacturer)
        self.speed = speed
        self.capacity = capacity

    def __str__(self):
        return f"{super().__str__()}, speed: {self.speed}, capacity: {self.capacity}"

    def validate(self):
        return self.speed.isnumeric() and self.capacity.isnumeric()


storage = Storage()

computer = Computer('def_apfel', 12345, 'samsung', '123', '456')
print(computer)
wrong_computer = Computer('def_apfel', 3333, 'samsung', 'asd', 'qwe')
storage.add_product(computer)

try:
    storage.add_product(wrong_computer)
except Exception as e:
    print(e)

scaner = Scaner('xerox', 434, 'LG', '123', '456')
print(scaner)
wrong_scaner = Scaner('xerox', 333, 'LG', 'ddd', 'fff')
storage.add_product(scaner)

try:
    storage.add_product(wrong_scaner)
except Exception as e:
    print(e)

shreder = Shreder('creator', 999, 'samsung', '123', '456')
print(shreder)
wrong_shreder = Shreder('creator', 9898, 'samsung', 'asd', 'qwe')
storage.add_product(shreder)

try:
    storage.add_product(wrong_shreder)
except Exception as e:
    print(e)

print(storage)
storage.move_product_to_department(999, 'HR')
print(storage)
