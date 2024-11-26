###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')
a = int(a)
b = int(b)
c = int(c)
volume = a * b * c
surface_area = (a * b * 2) + (b * c * 2) + (a * c * 2)
print(f"Volume = {volume}, surface area = {surface_area}")