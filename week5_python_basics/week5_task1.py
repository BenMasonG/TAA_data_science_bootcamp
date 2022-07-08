'''
The purpose of this module is to idenfiy the users favourite meal
and print a statment stating what their favourite courses are.
'''

from decimal import Rounded


starter = input('What is your favourite starter?').lower()
main = input('What\'s your favourite main course?').lower()
dessert = input('What\'s your favourite dessert?').lower()
drink = input('What\'s your favourite drink').lower()

print('Your favourite meal is ' + starter + ' for your starter '
      + main + ' for your main course and', dessert +
      ' for desesert with a glass of', drink + ' to wash it down.')


#strech and challenge. Ask for bill and determine cost per person
bill = float(input('How much is the bill please?'))
number_of_diners = int(input('How many people are dinning?'))
cost_per_person = round(bill/number_of_diners, 2)

print(cost_per_person)
