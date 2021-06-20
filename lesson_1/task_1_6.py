while True:
    day=1
    distance = float(input("Enter distance for the first day: "))
    targetDistance = float(input("Enter the target distance: "))
    if distance < 0 or targetDistance <0:
        break
    while distance < targetDistance:
        day += 1
        distance *= 1.1
    print("you'll got your target on the %d day" % (day))