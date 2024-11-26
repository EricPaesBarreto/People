###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = input('Enter the text: ')
encrypted_text = ''
func = input('Decrypt or Encrypt? D/E: ')
if func == 'E':
    for char in plain_text:
        # read the character's code (use ord())
        code = ord(char)
        # add one to the character's code
        if char != ' ':
            code += 1
        # replace new character code with its
        # corresponding character (use chr())
        encrypted_text += chr(code)
        # add encrypted character to encrypted text
elif func == 'D':
    for char in plain_text:
        # read the character's code (use ord())
        code = ord(char)
        # add one to the character's code
        if char != ' ':
            code -= 1
        # replace new character code with its
        # corresponding character (use chr())
        encrypted_text += chr(code)
        # add encrypted character to encrypted text
else:
    print ('...')
print(plain_text)
print(encrypted_text)