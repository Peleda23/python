import random


player_wins = 0
computer_wins = 0
wininig_score = 2

while player_wins < wininig_score and computer_wins < wininig_score:
    print(f"Players score: {player_wins} Computers score: {computer_wins}")
    print(".....Rock.....")
    print(".....Paper.....")
    print(".....Scissors.....")
    player = input('(Player 1"s choice): ').lower()
    if player == "quit" or player == "q":
        break
    num = random.randint(1, 3)

    if num == 1:
        computer = "rock"
    elif num == 2:
        computer = "paper"
    else:
        computer = "scissors"

    print(f'(Computers 1"s choice): {computer}')

    if player == computer:
        print("It is a tie")
    elif player == "paper":
        if computer == "rock":
            print("Player wins!!!")
            player_wins += 1
        elif computer == "scissors":
            print("Computer wins!!!")
            computer_wins += 1
    elif player == "rock":
        if computer == "paper":
            print("Computer wins!!!")
            computer_wins += 1
        elif computer == "scissors":
            print("Player wins")
            player_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("Computer wins!!!")
            computer_wins += 1
        elif computer == "paper":
            print("Player wins!!!")
            player_wins += 1
    else:
        print("Something went wrong!!!")
if player_wins > computer_wins:
    print(f"Congratulations you win! Your score is {player_wins}")
elif player_wins == computer_wins:
    print("It is a tie!!!")
else:
    print(f"Oh no the computer wins! Computers score is {computer_wins}")


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
