'''
This module is for task 5: string modification.
'''

test_string = "This is a test string"

lower_test_string = test_string.lower() #will convert to lowercase
upper_test_string = test_string.upper() #will convert to uppercase
split_test_string = test_string.split() #will split string into a list
slice_test_string = test_string[10:14] #will return values at specified indexs
find_test_string = test_string.find("test") #finds specified string
title_test_string = test_string.title() #capitalse each first letter

print(lower_test_string)
print(upper_test_string)
print(split_test_string)
print(slice_test_string)
print(find_test_string)
print(title_test_string)
