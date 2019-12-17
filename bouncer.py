# ask for age
age = input("How old are you: ")

# visi skaiciai ivesti per input buna kaip string
# tada reikia juos konvertuoti i skaiciu su int()
# tkrinam ar nera empty string
if age != "":
    age = int(age)
    # 18-21 wristband
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband!")
    # 21+ drink, normal entry
    elif age >= 21:
        print("You good to enter and can drink!")
    # Too young sorry
    else:
        print("You too young!!!")
else:
    print("Please enter age!!!")
