###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# User enters the temp in Celsius
C = float(input('Enter the temperature in Celsius: '))
# Convertion to Kelvin and Fahrenheit
K = C + 273.15
F = C * (9/5) + 32
# Prints the result
print(f'Temperature in Kelvin: {K}\nTemperature in Fahrenheit: {F}')