#Numbers

import math
#in python you need to import funtions at times

num1 = 4

print(math.exp(num1))
#the exponential was part of the math function hence it was necessary to mention
# e^4

num2 = math.exp(4)

print(int(num2))
print(round(num2,2))
#to round the value to 2 decimal places

print(math.log10(num1))

num3 = math.log10(num1)

print(round(num3,3))
# round() function to print floats to a specific number of decimal points in Python

print(math.sqrt(49))

print(math.sin(90))
#python tells the value in rad so need to use angles according to that
print(math.sin(math.pi/2))

num4 = math.sin(math.pi/2)
print("{0:.2f}".format(num4)) 
print("{0:.3f}".format(num4))
#format() function to print floats to a specific number of decimal points in Python

print(math.cos(math.pi))

