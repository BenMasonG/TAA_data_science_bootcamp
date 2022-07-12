'''
The purpose of this module is to idenfiy the users favourite meal
and print a statment stating what their favourite courses are.
'''

name = input('What is your name?').title()
starter = input('What is your favourite starter?').lower()
main = input('What\'s your favourite main course?').lower()
dessert = input('What\'s your favourite dessert?').lower()
drink = input('What\'s your favourite drink').lower()

print('Your favourite meal is ' + starter + ' for your starter '
      + main + ' for your main course and', dessert +
      ' for desesert with a glass of', drink + ' to wash it down.')


#stretch and challenge. Ask for bill and determine cost per person
bill = float(input('How much is the bill please?'))
number_of_diners = int(input('How many people are dinning?'))
cost_per_person = round(bill/number_of_diners, 2)

print('The bill will be £' + str(cost_per_person), 'per person')

def favourite_meal(name, starter, main, dessert, drink):
    '''
    Tell people what a person's favourite meal is.

    :param name: string - the person's name.
    :param starter: string - their favourite starter.
    :param main: string - their favourite main course.
    :param dessert: string - their favourite dessert.
    :param drink: main - their favourite drink.

    return: string - a sentence stating the person's favourite meal.
    '''

    print ( name + '\'s', 'favourite meal is ' + starter + ' for their starter '
      + main + ' for their main course and', dessert +
      ' for their desesert with a glass of', drink + ' to wash it down.')

favourite_meal(name, starter, main, dessert, drink)
