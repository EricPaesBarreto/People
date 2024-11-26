import math
circumference = int(input('Enter tree circumference in cm: '))
cut_down = (circumference/math.pi >= 50)
print (f'Tree can be cut down: {cut_down}')