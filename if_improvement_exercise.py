#john bain
#selection improvement exercise
#26-06-12

month = int(input("Please enter a month as a number between 1-12: "))

if month < 1 or month > 12:
    print("{} is not a month number between 1-12".format(month))

if month == 1:
    print("The month you entered is January")
elif month == 2:
    print("The month you entered is February")
elif month == 3:
    print("The month you entered is March")
elif month == 4:
    print("The month you entered is April")
elif month == 5:
    print("The month you entered is May")
elif month == 6:
    print("The month you entered is June")
elif month == 7:
    print("The month you entered is July")
elif month == 8:
    print("The month you entered is August")
elif month == 9:
    print("The month you entered is September")
elif month == 10:
    print("The month you entered is October")
elif month == 11:
    print("The month you entered is November")
elif month == 12:
    print("The month you entered is December")
