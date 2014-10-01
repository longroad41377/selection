weights = [100, 50, 10, 5, 2, 1]

weight = int(input("Enter weight: "))

for curweight in weights:
    weightsUsed = weight // curweight
    weight = weight % curweight

    if weightsUsed:
        print("Number of {0}g weights needed: {1}".format(curweight, weightsUsed))
