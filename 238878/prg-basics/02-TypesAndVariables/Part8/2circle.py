###
# Calculation of circle area and circumference 
#
import math
# determine radius and PI values
r = int(input('Enter the radius of the circle: '))
# calculate area 
area = math.pi * r ** 2
# calculate circumference
circumference = 2 * math.pi * r
# print results
print(f'Area of the circle: {area:.2f}\nCircumference of the circle: {circumference:.2f}')