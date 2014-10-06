while True:
    mark = int(input("Enter mark: "))
    if mark < 0 or mark > 100:
        print("That mark is impossible")
    elif mark < 41:
        print("Grade: U")
    elif mark < 51:
        print("Grade: E")
    elif mark < 61:
        print("Grade: D")
    elif mark < 71:
        print("Grade: C")
    elif mark < 81:
        print("Grade: B")
    else:
        print("Grade: A")
