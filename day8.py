# def greet():
#     print('Hello')
#     print("Tomas")
#     print("Goodbay")

# greet()

# def greet_name(name):
#     print(f'Hello {name}')
#     print(f'How do you do {name}')

# greet_name('Tomas')

#Function with more than 1 input

# def greet_with(name, location):
#     print(f'Hello {name} from {location}.')

# greet_with('Tomas', 'Klaipeda')

#Write your code below this line 👇
# import math
# def paint_calc(height, width, cover):
#      number_of_cans = (height * width)/cover
#      number_of_cans = math.ceil(number_of_cans)
#      print(number_of_cans)

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

def prime_checker(number):
     is_prime = True
     for i in range(2, number):
          if number % i == 0:
               is_prime = False
     if is_prime:
          print("It's a prime number.")
     else:
          print("It's not a prime number")



n = int(input("Check this number: "))
prime_checker(number=n)
