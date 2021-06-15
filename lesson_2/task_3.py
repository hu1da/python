# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasones = dict()
seasones_list = ['winter', 'spring', 'summer', 'autumn']
seasones_dict = {}
i = 1
while i < 13:
    if i == 12 or i < 3:
        seasones_dict[i] = seasones_list[0]
    elif i < 6:
        seasones_dict[i] = seasones_list[1]
    elif i < 9:
        seasones_dict[i] = seasones_list[2]
    elif i < 12:
        seasones_dict[i] = seasones_list[3]
    i += 1

print(seasones_dict)
month_number = int(input("Enter a month number: "))

if month_number > 12 or month_number < 1:
    print('month number should be between 1 and 12')
else:
    print('the season is: ', seasones_dict[month_number])
