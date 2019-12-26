import random

print(".....Rock.....")
print(".....Paper.....")
print(".....Scissors.....")

player = input('(Player 1"s choice): ').lower()
num = random.randint(1, 3)

if num == 1:
    computer = 'rock'
elif num == 2:
    computer = 'paper'
else:
    computer = 'scissors'

print(f'(Computers 1"s choice): {num}')

if player == computer:
    print('It is a tie')
elif player == 'paper':
    if computer == 'rock':
        print('Player wins!!!')
    elif computer == 'scissors':
        print('Computer wins!!!')
elif player == 'rock':
    if computer == 'paper':
        print('Computer wins!!!')
    elif computer == 'scissors':
        print('Player wins')
elif player == 'scissors':
    if computer == 'rock':
        print('Computer wins!!!')
    elif computer == 'paper':
        print('Player wins!!!')    
else:
    print('Something went wrong!!!')                                                

# if player_one == player_two:
#     print('It is a tie')
# elif player_one == 'rock':
#     if player_two == 'scissors':
#         print('Player 1 wins!!!')
#     elif player_two == 'paper':
#         print('Player 2 wins!!!')
# elif player_one == 'paper' :
#     if player_two == 'rock':
#         print('Player 1 wins!!!')
#     elif player_two == 'scissors':
#         print('Player 2 wins!!!')
# elif player_one == 'scissors':
#     if player_two == 'paper':
#         print('Playrer 1 wins!!!')
#     elif player_two == 'rock':
#         print('Player 2 wins!!!')
# else:
#     print('Something went wrong')        
                                    


# if player_one == "rock" and player_two == "scissors":
#     print("Player 1 wins")
# elif player_one == "rock" and player_two == "paper":
#     print("Player 2 wins")
# elif player_one == "paper" and player_two == "rock":    
#     print('Player 1 wins!')
# elif player_one == "paper" and player_two == "scissors":
#     print("Player 2 wins!")
# elif player_one == "scissors" and player_two == "rock":
#     print("Player 2 wins!")
# elif player_one == "scissors" and player_two == "paper":
#     print("Player 1 wins!")            
# elif player_one ==  player_two:
#     print("It is a tie!")
# else:
#     print("Something went wrong")
