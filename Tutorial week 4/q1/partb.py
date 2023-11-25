import random

hidden = random.randint(1,20)
user_input = input("Guss a number between 1 and 20:")

try:
    while(int(user_input)!= hidden):
        print(f"Sorry {user_input} is not the correct number")
        user_input = input("Guess a number between 1 and 20:")
    print(f"{user_input} was correct")
except ValueError as error:
    print("Please enter vaild number")


    