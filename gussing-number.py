import random

random_number = random.randint(0,9)

guess = 0

print("This is very interesting game. My program has generated a randrom number between 0 - 9 and you just need to guess that number")
print('IMPORTANT: You have only 4 attempts to guess.')
print("You can type 'exit' to quit this game")
tries = 0
while guess != random_number:

    guess = input('What did you guess: ')

    if guess == 'exit':
        break

    guess = int(guess)

    tries += 1

    if guess < random_number:
        print('Very low')
    elif guess > random_number:
        print('Very high')
    else:
        print('Congratulations! You got it in just ' + str(tries) + ' attempts')

    if tries == 4:
        print('Sorry! you have lost the game')
        break


