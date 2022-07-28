'''
This module is a basic GUI for task 2 of the week 7 Home Learning Tasks.
'''

import tkinter as tk

fruit_list = []

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
        frm_entry.delete(0, tk.END)
        lbl_result['text'] = f'There is 1 vowel in the word {fruit}'
        return f'There is 1 vowel in the word {fruit}'
    if count_vowels > 1:
        frm_entry.delete(0, tk.END)
        lbl_result['text'] = f'There are {count_vowels} vowels in the word {fruit}'
        return f'There are {count_vowels} vowels in the word {fruit}'
    if count_vowels == 0:
        frm_entry.delete(0, tk.END)
        lbl_result['text'] = f'There are {count_vowels} vowels in the word {fruit}'
        return f'There are {count_vowels} vowels in the word {fruit}'

def add_to_list():
    '''
    This function adds a word to a list. This list is displayed in the GUI.
    When the function is called after the word is added to the list the entry
    form is cleared so a new word can be added. The word list display is updated
    each time the function is called.
    '''
    word = add_entry.get()
    fruit_list.append(word)
    current_list['text'] = fruit_list
    add_entry.delete(0, tk.END)

def gui_list_vowel_count ():
    '''
    A function to iterate through a list of fruits and return the number of vowels
    in each fruit.

    The word list is taken from the words displayed in the GUI. The user adds words
    to the list by pressing the add to list button. When The process button is pressed
    this funtion runs and returns a list of detailing the number of vowels in each
    word in the function.
    '''
    vowels_per_fruit = []
    for fruit in fruit_list:
        vowels_per_fruit.append(vowel_counter(fruit))
    fruit_list.clear()
    current_list['text'] = fruit_list
    vowels_in_list['text'] = vowels_per_fruit

window = tk.Tk()
window.columnconfigure(0, minsize=300)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=50)

btn_start = tk.Button(text='Count Vowels', command=gui_vowel_count)
frm_entry = tk.Entry()
lbl_result = tk.Label()
btn_add = tk.Button(text='Add to list', command=add_to_list)
add_entry = tk.Entry()
current_list = tk.Label()
btn_process = tk.Button(text='Process List', command=gui_list_vowel_count)
vowels_in_list = tk.Label()

btn_start.grid(row=0, column=0, sticky='nsew')
frm_entry.grid(row=1, column=0)
lbl_result.grid(row=2, column=0)
btn_add.grid(row=3, column=0, sticky='nsew')
add_entry.grid(row=4, column=0)
current_list.grid(row=5, column=0)
btn_process.grid(row=6, column=0, sticky='nsew')
vowels_in_list.grid(row=7, column=0)

window.mainloop()
