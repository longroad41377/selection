import re
import leapyear

while True:
    date = input("Enter date: ")

    match = re.match("(\d{1,2}) (\d{1,2}) (\d{2})$", date)

    if not match:
        print("Invalid date")
    else:
        day = int(match.group(1))
        month = int(match.group(2))
        year = int(match.group(3))

        invalidday = False

        if day < 1:
            invalidday = True
        else:
            if month == 2:
                if leapyear.IsLeapYear(year):
                    maxday = 29
                else:
                    maxday = 28
            else:
                if month < 8:
                    if month % 2:
                        maxday = 31
                    else:
                        maxday = 30
                else:
                    if not month % 2:
                        maxday = 31
                    else:
                        maxday = 30
            if day > maxday:
                invalidday = True

        sufix = "th"
        if day // 10 != 1:
            if day % 10 == 1:
                sufix = "st"
            elif day % 10 == 2:
                sufix = "nd"
            elif day % 10 == 3:
                sufix = "rd"

        day = str(day) + sufix
        if invalidday:
            day += " (non-existant day)"

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
