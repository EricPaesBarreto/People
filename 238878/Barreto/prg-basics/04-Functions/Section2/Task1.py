###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

key_stroke = input('Input: ')
print('The key you pressed was: ', key_stroke)

num_string = ascii('20303')
print('The number representing the string [20303] is: ', num_string)

bin_num = bin(304)
print('The binary representation of the denary value [304] is: ', bin_num)

hex_num = hex(304)
print('The hex representation of the denary value [304] is: ', hex_num)

unicode_int = '€'.decode("utf-8")
print('The unicode representation of the € sign is: ', unicode_int)

abs_num = abs(-17)
print('The absolute value of [-17] is: ', abs_num)