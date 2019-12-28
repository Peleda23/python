import random

random_number = random.randint(1,10)  # numbers 1 - 10

while True:
    user_guess = int(input('Guess a number between 1 and 10: '))
    user_guess = int(user_guess)
    if user_guess == random_number:
        print('You guessed it! You won!')
        user_exit = input('Do you want keep playing?  (y/n) ')
        if user_exit == 'y':
            random_number = random.randint(1,10)  
            user_guess = None
        else:
            break
    elif int(user_guess) > random_number:
        print('Your number is to hight!')
    elif int(user_guess) < random_number:
        print('Your number is to low!') 
    

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!