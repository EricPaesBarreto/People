###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character)
#
university = 'Krakow University of Economics'
university_expanded = ''
i = 1
for char in university:
    if i != len(university) and char != ' ':
        university_expanded += char + ' '
    else:
        university_expanded += char
    i += 1
    

print(university)
print(university_expanded)