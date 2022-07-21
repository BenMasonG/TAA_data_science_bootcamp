def calculator():
    '''
    This is a function that takes two numbers and then performs the requested
    calculation on them.

    :param num1: float - A number previous input by the user.
    :param num2: float - A number previous input by the user.
    :param op: str - A basic math op previosuly input by the user.
    :return: If the input params the result of the requested calculation will
    be returned. Else an error message will be given to the user.

    This function is a basic calculator that takes two numbers and performs a calulation.
    '''

    num1 = float(input('please select a number'))
    num2 = float(input('please select a number'))
    op = str(input('please select an operator'))

    #Only if statements used as if any statement is true an outcome will be returned
    #to the user. This will break the function so any use of elif would be supflerous.
    #else used at the end to avoid raising an error when the function is intially
    #run in the interactive terminal.

    if isinstance(num1, float) is not True and isinstance(num1, int) is not True:
        raise TypeError('The first paramater must be a number')
    if isinstance(num2, float) is not True and isinstance(num2, int) is not True:
        raise TypeError('The second paramater must be a number')
    if op == '*':
        return f'{num1} * {num2} = {num1 * num2}'
    if op == '/':
        return f'{num1} / {num2} = {num1 / num2}'
    if op == '+':
        return f'{num1} + {num2} = {num1 + num2}'
    if op == '-':
        return f'{num1} - {num2} = {num1 - num2}'
    if op == '**':
        return f'{num1} ** {num2} = {num1 ** num2}'
    if op == '//':
        return f'{num1} // {num2} = {num1 // num2}'
    if op == '%':
        return f'{num1} % {num2} = {num1 % num2}'
    if (op != '*' or op != '/' or op != '+' or op != '-' or
        op != '**' or op != '//' or op != '%'):
        raise TypeError('The third paramater must be a valid operator')
    else:
        raise Exception('Sorry, an unexpected error has occured. Please try again.')

calculator()
