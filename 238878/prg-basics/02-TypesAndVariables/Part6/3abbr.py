###
# A program that prints a university abbreviation
#   
university = input("Input uni name here: ")
words = university.split()
initials = ""
for word in words:
        if word[0].isupper():
            initials += word[0]
print(initials)