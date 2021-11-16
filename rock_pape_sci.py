rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scisors.\n "))

comp_choise = random.randint(0, 2)
print(comp_choise)

if choise == 0:
  print(rock)
elif choise == 1:
  print(paper)
else:
  print(scissors)   

print("Computer choise:")

if comp_choise == 0:
  print(rock)   
elif comp_choise == 1:
  print(paper)
else:
  print(scissors)   

if choise == 0:
  if comp_choise == 0:
    print("Draw!!!")
  elif comp_choise == 1:
    print("Computer Won!!!")
  else:
    print("You Won!!!") 

if choise == 1:
  if comp_choise == 0:
    print("You Won!!!")
  elif comp_choise == 1:
    print("Draw!!!")
  else:
    print("Computer Won!!!")

if choise == 2:
  if comp_choise == 0:
    print("Computer Won!!!")
  elif comp_choise == 1:
    print("You Won!!!")
  else:
    print("Draw!!!")
