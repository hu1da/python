# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
aggregate_dictionary = dict()
for el in my_list:
    aggregate_dictionary[el] = (1 if aggregate_dictionary.get(el) == None else aggregate_dictionary.get(el) + 1)
new_list = [el for el in aggregate_dictionary if aggregate_dictionary.get(el) == 1 ]
print(my_list)
print(new_list)
