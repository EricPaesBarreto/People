###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#

import random
game = True
while game:
    # COMPUTER TURN
    computer = random.randint(1,6)
    # YOUR TURN
    you = int(input('Your guess: '))
    print(f"Computer's number: {computer}")
    if you == computer:
        print('You won!')
        game = False
    else:
        print('You lost!')