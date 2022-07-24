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
vowel_counter(123)
