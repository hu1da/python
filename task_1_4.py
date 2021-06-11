while True:
    number = int(input("Enter your number: "))
    if number == 'stop':
        break
    max = -1
    current = None
    while  number >= 1:
        current = number%10
        number = int(number/10)

        if max < current:
            max=current
    print("the answer is: %s" % max)
