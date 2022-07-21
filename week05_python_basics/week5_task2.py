'''
This module is for task 2: calculations. I will practice using python
to do math.
'''
import math

#floats will be used for the data type to ensure there is no error if the user
#enters a float as opposed to an integer.

number_1 = float(input('Please enter a number'))
number_2 = float(input('Please enter a number'))

subtraction = number_1 - number_2
print(subtraction)

number_3 = float(input('Please enter a number'))
number_4 = float(input('Please enter a number'))

multiplication = number_3 * number_4
print(multiplication)

number_5 = float(input('Please enter a number'))
number_6 = float(input('Please enter a number'))

division = number_5 / number_6
print(division)

modulus = number_5 % number_2
print(modulus)

expnentiation = number_2**number_6
print(expnentiation)

floor_division = number_6 // number_1
print(floor_division)

power_of = pow(number_1, number_3)
print(power_of)

#stretch and challenge
#I have seen different formulas for surface area so this may not be correct
radius = float(input('What is the radius?'))
depth = float(input('What is the depth?'))
total_volume = math.pi * radius * radius * depth
surface_area = ((2*math.pi*radius) * depth) + ((math.pi*radius**2)*2)

print('The total volume of is: ', round(total_volume, 3))
print('The surface area is: ', round(surface_area, 3))
