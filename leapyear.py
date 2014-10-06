year = int(input("Enter year number: "))

leapyear = False
if not year % 4:
    if year % 100:
        leapyear = True
    else:
        if not year % 400:
            leapyear = True

if leapyear:
    print("That is a leap year")
else:
    print("That is not a leap year")
