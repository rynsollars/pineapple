__author__ = 'ryansollars'

import sys
import random
secret_number = random.randint(2, 20)
print 'I am thinking of a number between 1 and 20.'
print 'But, you only get 6 guesses'

for guesses_taken in range(1, 7):
    print 'Take a guess'
    guess = int(input())

    if guess < secret_number:
        print 'Your guess is to low.'
    elif guess > secret_number:
        print 'Your guess is to high.'
    else:
        break

if guess == secret_number:
    print('Congratulations, you are correct! It only took you ' + str(guesses_taken) + ' tries!')
else:
    print('Nope, the number I was thinking of was ' + str(secret_number))
sys.exit()