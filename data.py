import re

date = input("Enter date: ")

match = re.match("(\d{1,2}) (\d{1,2}) (\d{2})$", date)

if not match:
    print("Invalid date")
else:
    day = int(match.group(1))
    month = int(match.group(2))
    year = int(match.group(3))

    if day % 10 == 1:
        sufix = "st"
    elif day % 10 == 2:
        sufix = "nd"
    elif day % 10 == 3:
        sufix = "rd"
    else:
        sufix = "th"

    day = str(day) + sufix

    monthnames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if month > 0 and month <= 12:
        month = monthnames[month-1]
    else:
        month = "Invalid Month"

    if year > 30:
        year = str(1900 + year)
    else:
        year = str(2000 + year)

    print("{0} {1} {2}".format(day, month, year))
