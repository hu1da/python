# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

products = []
statistics = dict(name=set(), price=set(), quantity=set(), units=set())
index = 0
while True:
    answer = input("To insert new product press 1.\nTo print statistics and exit programm press any key: ")
    if answer == '1':
        name = input("enter product name: ")
        price = input("enter price: ")
        quantity = input("enter quantity: ")
        units = input("enter units: ")

        products.append((index, {'name': name, 'price': price, 'quantity': quantity, 'units': units}))
        index += 1
    else:
        current = 0
        length = len(products)
        while current < length:
            statistics['name'].add(products[current][1]['name'])
            statistics['price'].add(products[current][1]['price'])
            statistics['quantity'].add(products[current][1]['quantity'])
            statistics['units'].add(products[current][1]['units'])
            current += 1
        break
print(products)
print(statistics)
