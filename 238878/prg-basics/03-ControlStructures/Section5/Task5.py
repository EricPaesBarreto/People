###
# Sums numbers entered by user
#
total_sum = 0
avr = 0
i = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        avr = total_sum / i
        break  # Exit the loop when 0 is entered
    total_sum += number
    i += 1

print(f"The total sum of the numbers is: {total_sum}")
print(f'Avr: {avr}')