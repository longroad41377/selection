weight = int(input("Enter weight: "))

hundred = weight // 100
remainder = weight % 100

fifty = remainder // 50
remainder = remainder % 50

ten = remainder // 10
remainder = remainder % 10

five = remainder // 5
remainder = remainder % 5

two = remainder // 2
remainder = remainder % 2

one = remainder

print("""Number of 100g weights needed: {0}
Number of 50g weights needed: {1}
Number of 10g weights needed: {2}
Number of 5g weights needed: {3}
Number of 2g weights needed: {4}
Number of 1g weights needed: {5}""".format(hundred, fifty, ten, five, two, one))
