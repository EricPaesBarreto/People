###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter second letter: ')
first_letter_code = ord(first)
second_letter_code = ord(last)
number_of_letters = second_letter_code - first_letter_code
if number_of_letters != 0:
    number_of_letters = abs(number_of_letters) - 1
print(f'Between {first} and {last} are {number_of_letters} letters')