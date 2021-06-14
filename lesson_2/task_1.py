# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


array_like_structure = [42, 3.14,
                        complex(4, 2),
                        "don't panic",
                        list('I am a list'),
                        tuple('I am a tuple'),
                        set('I am a set'),
                        frozenset('I am a frozenset'),
                        dict(who='I am', name='a dicitonary')
    , False, None]

for el in array_like_structure:
    print(type(el), ": ", el)
