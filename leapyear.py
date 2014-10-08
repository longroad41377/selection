def IsLeapYear(year):
    leapyear = False
    if not year % 4:
        if year % 100:
            leapyear = True
        else:
            if not year % 400:
                leapyear = True
    return leapyear
