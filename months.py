monthnames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month = int(input("Enter month number: "))

if month > 0 and month < 13:
    print("Month name: {}".format(monthnames[month-1]))
else:
    print("Month number must be between 1 and 12")
    
