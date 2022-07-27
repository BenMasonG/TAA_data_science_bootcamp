'''
This module is for task 2 of the week 7 Home Learning Tasks.
'''

import tkinter as tk

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
        return f'There are {count_vowels} vowels in the word {fruit}'

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


def gui_vowel_count():
    '''
    This funtion takes a string and returns the number of values in the string.
    There word string can be input by the user via the GUI. After entering a word
    the user needs to press the Count Vowels button to run the program.

    :return: The number of vowels in that fruit.
    '''
    fruit = frm_entry.get()
    count_vowels = 0
    for letter in fruit:
        if letter.lower() in 'aeiou':
            count_vowels += 1
    if count_vowels == 1:
        lbl_result['text'] = f'There is 1 vowel in the word {fruit}'
        return f'There is 1 vowel in the word {fruit}'
    if count_vowels > 1:
        lbl_result['text'] = f'There are {count_vowels} vowels in the word {fruit}'
        return f'There are {count_vowels} vowels in the word {fruit}'
    if count_vowels == 0:
        lbl_result['text'] = f'There are {count_vowels} vowels in the word {fruit}'
        return f'There are {count_vowels} vowels in the word {fruit}'

window = tk.Tk()
window.columnconfigure(0, minsize=300)
window.rowconfigure([0, 1, 2], minsize=50)

btn_start = tk.Button(text='Count Vowels', command=gui_vowel_count)
frm_entry = tk.Entry()
lbl_result = tk.Label()

btn_start.grid(row=0, column=0, sticky='nsew')
frm_entry.grid(row=1, column=0)
lbl_result.grid(row=2, column=0)

window.mainloop()
