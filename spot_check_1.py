from math import pi

width = float(input("Enter width of pool: "))
length = float(input("Enter length of pool: "))
depth = float(input("Enter depth of pool: "))

mainSectionVolume = length * width * depth
circleRadius = width / 2
circleArea = pi * circleRadius**2
halfCircleVolume = (circleArea / 2) * depth
poolVolume = mainSectionVolume + halfCircleVolume

print("Volume of pool is: {}".format(poolVolume))
