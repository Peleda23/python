print('.....Rock.....')
print('.....Paper.....')
print('.....Scissors.....')

player_one = input('(enter Player 1"s choice): ')
player_two = input('(enter Player 2"s choice): ')

print('The game is on!!!')

if player_one == 'rock' and player_two == 'paper':
    print('Player 2 wins')
elif player_one == 'paper' and player_two == 'scissors':
    print('Player 2 wins')
elif player_one == 'scissors' and player_two == 'rock':
    print('Player 2 wins')
else:
    print('Player 1 wins')
