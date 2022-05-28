# This is a guess the number game

import random

secretNumber = random.randint(1,20)
print("I'm thinking of a number between 1 and 20")

# Ask player for up to 6 guesses
for guessesTaken in range(1,7):
	print('Take a guess:')
	guess = int(input())

	if guess < secretNumber:
		print('Your guess is too low.')
	elif guess > secretNumber:
		print('Your guess iss too high.')
	else:
		break	# Guess was correct

if guess == secretNumber:
	print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
	print('Sorry, the number I was thinking of was ' + str(secretNumber))
