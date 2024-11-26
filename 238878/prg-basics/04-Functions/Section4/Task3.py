###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
def triangle_area(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

print(f'The area of ​​a triangle with sides {a}, {b} ,{c} is {triangle_area(a,b,c)}')
