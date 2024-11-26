###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number = str(number)
    sum = 0
    for char in number:
        sum += int(char)
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')