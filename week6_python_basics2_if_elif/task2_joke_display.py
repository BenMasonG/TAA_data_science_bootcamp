
def random_joke():
    '''
    The functions asks the user for a number between 1 and 100. 1 of 3 jokes
    is then told to the user based on what number the give. If the number is
    not between 1 and 100 an error message is shown to the user.
    '''
    number =  input('What is your favourite number between 1 and 100?')
    joke1 = 'I am a realy funny joke.'
    joke2 = 'I am an even funnier joke'
    joke3 ='I am the funniest joke of all.'

    if int(number) > 100 or int(number) <= 0:
        raise ValueError('The number should be between 1 and 100.')
    if int(number) >66:
        return joke1
    if int(number) >33:
        return joke2
    if int(number) >0:
        return joke3
    else:
        raise Exception('Error. Please make sure you input a number between 1 and 100')

random_joke()
