'''
The purpose of this module is to idenfiy the users favourite meal
and print a statment stating what their favourite courses are.
'''

starter = input('What is your favourite starter?').lower()
main = input('What\'s your favourite main course?').lower()
dessert = input('What\'s your favourite dessert?').lower()
drink = input('What\'s your favourite drink').lower()

print('Your favourite meal is ' + starter + ' for your starter '
      + main + ' for your main course and', dessert +
      ' for desesert with a glass of', drink + ' to wash it down.')
