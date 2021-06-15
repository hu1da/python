sec_in_hour = 3600
sec_in_min = 60
time_sec = 0
while True:
    time_sec = int(input("enter time in seconds: "))
    if time_sec < 0:
        break
    else:
        hours = time_sec // sec_in_hour
        minutes = time_sec % sec_in_hour // sec_in_min
        seconds = time_sec % sec_in_min

        print("your time is: {:,d}:{:0>2d}:{:0>2d}".format(hours, minutes, seconds))
