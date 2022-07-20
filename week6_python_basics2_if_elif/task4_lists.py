'''
This module is to complete the lists exercise as part of the homework for this
week.
'''
fruits = ('bannana', 'orange', 'apple')
print(fruits[1])

fruits2 = set(fruits)
print(fruits2)

fruits2.add('cherries')
print(fruits2)

fruits2.add('cherries')
print(fruits2)

fruit_price = {
    'bannana': '£2.52',
    'orange': '£1.30',
    'apple': '50p',
    'cherries': '£3.30'
}

print(fruit_price)

print(fruit_price['orange'])


def check_price (fruit):
    '''
    This allows the user to check the price of a fruit. If the fruit requested is not available
    the user will be given a list of the availabl fruits.

    :param fruit: str - the fruit the user wants the price of.
    :result: the price of the fruit if it is available or a list of available fruits.
    '''
    if fruit in fruit_price.keys():
        return fruit_price[fruit]
    return f'Sorry the price of that item is unavailable. The available fruit\
        are {fruit_price.keys()}'

check_price('orange')

#The below function is to demonstrate the use of a for loop.
def all_prices():
    '''
    This funcition returns the price of all fruits in the fruit price list
    '''
    for fruit in fruit_price:
        if fruit[-1] == 's':
            print(f'{fruit} cost {fruit_price[fruit]}.')
        else:
            print(f'{fruit}s cost {fruit_price[fruit]}.')

all_prices()
#