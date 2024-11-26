###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
length = len(phone)
if length < 9:
    print("Number has less than 9 numbers.")
elif length > 9:
    print("Number has more than 9 numbers.")
else:
    print(f'Phone number: {phone[:3]}-{phone[3:6]}-{phone[6:]}')