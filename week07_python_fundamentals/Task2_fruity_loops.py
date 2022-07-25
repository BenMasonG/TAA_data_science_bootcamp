'''
This module is for task 2 of the week 7 Home Learning Tasks. 
'''
def vowel_counter(fruit):
    '''
    This funtion takes a string and returns the number of values in the string.
    :param fruit: str - the name of a fruit.
    :return: The number of vowels in that fruit.
    '''

    if not isinstance(fruit, str):
        raise TypeError('This function only accept strings as an argument')
    count_vowels = 0
    for letter in fruit:
        if letter.lower() in 'aeiou':
            count_vowels += 1
    if count_vowels == 1:
        return f'There is 1 vowel in the word {fruit}'
    if count_vowels > 1:
        return f'There are {count_vowels} vowels in the word {fruit}'
    if count_vowels == 0:
        return 'Wow, you found a fruit that has no vowels in its name!'

vowel_counter('Banana')
vowel_counter('Orange')
vowel_counter('Pear')
vowel_counter('zzzz')


def list_vowel_counter(fruit_list):
    '''
    A function to iterate through a list of fruits and return the number of vowels
    in each fruit.

    :param fruit_list: list of str - a list of strings.
    :return: A list stating how many vowels were in each string in the inital list
    '''

    vowels_per_fruit = []
    for fruit in fruit_list:
        vowels_per_fruit.append(vowel_counter(fruit))
    return vowels_per_fruit

list_of_fruits = ['apple', 'banana', 'pear']

list_vowel_counter(list_of_fruits)
