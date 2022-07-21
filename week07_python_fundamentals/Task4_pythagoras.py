from math import sqrt, hypot

def pythagoras_theorem(side_a, side_b, side_c):
    '''
    This function takes three inputs. Two are known side lengths of a right
    angle triangle and the third is '?'. The '?' can be any paramater and
    represents an unknown length. The function returns the length of the 
    unknown paramater.
    
    :param side_a: int, float or string -This is one of the shorter sides of
    the triangle. If the value is known the input should be an int or flaot.
    If the value is unknown it should be '?'.
    :param side_b: int, float or string -This is one of the shorter sides of
    the triangle. If the value is known the input should be an int or flaot.
    If the value is unknown it should be '?'.
    :param side_c: int, float or string -This is the longer side of the
    triangle. If the value is known the input should be an int or flaot.
    If the value is unknown it should be '?'.
    :return: int or float - the length of the unknown side.

    This function will take the length of two sides of a right angled triangle
    and use Pythagorean therem to return the length of the unknown side. 
    '''
    if (side_a == '?' and side_b == '?') or (side_a == '?' and side_c == '?')\
        or (side_b == '?' and side_c == '?'):
            raise ValueError('Only one input can be unknown.')
    if side_a == '?':
        unknown_side = sqrt((side_c * side_c) - (side_b * side_b))
        return f'Side a equals {unknown_side}.'
    if side_b == '?':
        unknown_side = sqrt((side_c * side_c) - (side_a * side_a))
        return f'Side b equals {unknown_side}'
    if side_c == '?':
        unknown_side = hypot(side_a, side_b)
        return f'Side c equals {unknown_side}'

pythagoras_theorem('?', 3, 6)
pythagoras_theorem(3, '?', 6)
pythagoras_theorem(3, 3, '?')
