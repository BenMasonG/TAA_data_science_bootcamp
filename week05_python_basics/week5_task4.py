'''
This module is for task 4: casting.
'''

number_1 = float(input('Please enter a number'))
number_2 = float(input('Please enter a number'))
multiply = number_1 * number_2

#print statment split over 2 lines to abide by PEP8 line length conventions
print(int(multiply), float(multiply), str(multiply), bool(multiply),
      memoryview(bytes(int(multiply))), bytes(int(multiply)))
