def vowel_counter(fruit):
    count_vowels = 0
    for letter in fruit:
        if letter.lower() in 'aeiou':
            count_vowels += 1
    if count_vowels == 1:
        return f'There is 1 vowel in the word {fruit}'
    if count_vowels > 1:
        return f'There are {count_vowels} vowels in the word {fruit}'
    if count_vowels == 0:
        return f'Wow, you found a fruit that has 0 vowels in its name!'
