proceeds = float(input("enter your proceeds: "))
expencies = float(input("enter your expencies: "))
profit = proceeds - expencies
print("your firm gained: %d" % (profit))

employeesNumber = float(input("how many employees are working at the firm?"))
print("ther profit per employee is: %d" % (profit/employeesNumber))

