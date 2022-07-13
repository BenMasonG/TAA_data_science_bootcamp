'''
This module is for task 2: calculations. I will practice using python
to do math.
'''

import math

#floats will be used for the data type to ensure there is no error if the user
#enters a float as opposed to an integer.

number1 = float(input('Please enter a number'))
number2 = float(input('Please enter a number'))
number3 = float(input('Please enter a number'))
number4 = float(input('Please enter a number'))
number5 = float(input('Please enter a number'))
number6 = float(input('Please enter a number'))

def subtraction(num1, num2):
    '''
    Subtracts number1 from number2.

    :param num1: float - any number.
    :param num2: float - any number.
    :return: str - the calculation performed and the answer.

    This functions allows you to subtract one number from another
    and see the answer.
    '''
    answer = num1 - num2
    return f'{num1} - {num2} = {answer}'

subtraction(number1, number2)

def addition(num1, num2):
    '''
    Adds number1 to number2.

    :param num1: float - any number.
    :param num2: float - any number.
    :return: str - the calculation performed and the answer.

    This functions allows you to add one number to another
    and see the answer.
    '''
    answer = num1 + num2
    return f'{num1} + {num2} = {answer}'

addition(number3, number4)

def multiplication(num1, num2):
    '''
    Times number1 by number2.

    :param num1: float - any number.
    :param num2: float - any number.
    :return: str - the calculation performed and the answer.

    This functions allows you to times one number by another
    and see the answer.
    '''
    answer = num1 * num2
    return f'{num1} * {num2} = {answer}'

multiplication(number5, number6)

def division(num1, num2):
    '''
    Divide number1 by number2.

    :param num1: float - any number.
    :param num2: float - any number.
    :return: str - the calculation performed and the answer.

    This functions allows you to divide one number by another
    and see the answer.
    '''
    answer = num1 / num2
    return f'{num1} / {num2} = {answer}'

division(number2, number6)

def modulus(num1, num2):
    '''
    Find the modulus of number1 divided by number2.

    :param num1: float - any number.
    :param num2: float - any number.
    :return: str - the calculation performed and the answer.

    This functions allows you to divide one number by another
    and find the modulus.
    '''
    answer = num1 % num2
    return f'{num1} % {num2} = {answer}'

modulus(number3, number1)

def floor_division(num1, num2):
    '''
    Divide number1 by number2 and return the largest possible integar.

    :param num1: float - any number.
    :param num2: float - any number.
    :return: str - the calculation performed and the answer.

    This functions allows you to divide one number by another
    and see the answer and return the largest possible integar
    '''
    answer = num1 // num2
    return f'{num1} // {num2} = {answer}'

floor_division(number2, number6)

def exponentiation(num1, num2):
    '''
    Raise num1 to the power of num2.

    :param num1: float - any number.
    :param num2: float - any number.
    :return: str - the calculation performed and the answer.

    This functions allows you to raise a number to the power of another
    number and see the calulation and result.
    '''
    answer = num1 ** num2
    return f'{num1} ** {num2} = {answer}'

exponentiation(number2, number6)

def power_of(num1, num2):
    '''
    Raise num1 to the power of num2.

    :param num1: float - any number.
    :param num2: float - any number.
    :return: str - the calculation performed and the answer.

    This functions allows you to raise a number to the power of another
    number and see the calulation and result.
    '''
    answer = pow(num1, num2)
    return f'{num1} to the power of {num2} = {answer}'

power_of(number2, number6)

#stretch and challenge
#I have seen different formulas for surface area so this may not be correct
radius = float(input('What is the radius?'))
depth = float(input('What is the depth?'))

def cylinder_total_volume(radius, depth):
    '''
    This calculates the total volume of a cylinder.

    :param radius: float - the radois of the cylinder.
    :param depth: float - the depth of the cylinder.
    return: str - the total volume of the cylindr.

    This functions allows you to calculate the total volume of a cylinder.
    '''
    total_volume = math.pi * radius * radius * depth
    return f'The total volume of is: {round(total_volume, 3)}'

cylinder_total_volume(radius, depth)

def cylinder_surface_area(radius, depth):
    '''
    This calculates the surface area of a cylinder.

    :param radius: float - the radois of the cylinder.
    :param depth: float - the depth of the cylinder.
    return: str - the surface area of the cylindr.

    This functions allows you to calculate the surface of a cylinder.
    '''
    surface_area = ((2*math.pi*radius) * depth) + ((math.pi*radius**2)*2)
    return f'The surface area is: {round(surface_area, 3)}'

cylinder_surface_area(radius, depth)
