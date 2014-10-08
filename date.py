import re

date = input("Enter date: ")

match = re.search("^([0-9]+) ([0-9]+) ([0-9]+)$", date)

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
month = monthnames[month-1]

if year > 30:
    year = str(1900 + year)
else:
    year = str(2000 + year)

print("{0} {1} {2}".format(day, month, year))
