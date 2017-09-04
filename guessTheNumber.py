#This is a guess the number game.
import random
secretNumber = random.randint(1,20)
print('I\'m thinking of a number between 1 and 20. I\'ll give you 6 guesses.')
#Ask the player to guess 6 times
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low. Try again.')
    elif guess > secretNumber:
        print('Your giess is too high. Try again.')
    else:
        break #This condition is the correct guess.
if guess == secretNumber:
    print('That\'s right! You guessed my number in ' + str(guessesTaken) + ' tries.')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')
