while True:
    number = input("Enter your number: ")
    if number == 'stop':
        break
    number2 = number + number
    number3 = number2 + number

    print("the answer is: %d" % (int(number)+ int(number2) + int(number3)))
