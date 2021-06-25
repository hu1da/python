from sys import argv

script_name, hourly_rate, hours_count, bonus = argv

print('monthly salary: '(float(hourly_rate) * float(hours_count)) + float(bonus))
