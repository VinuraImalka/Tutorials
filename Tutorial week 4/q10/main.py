import random
random_number = random.randint(1,20)

def is_number():
    is_number = True
    while is_number:
        try:
            guess = int(input("Enter number between 1 and 20:"))
            is_number = False
            return guess
            continue
        except ValueError:
            print("Please enter number between 1 and 20")
            
for attempt in range (1,6):
    guess=is_number()
    is_in_range = True
    while is_in_range:        
        if 1 <= guess <= 20:
            is_in_range=False
            continue
        else:
            print("Please enter number between 1 and 20")
            guess = is_number()
                       
    if guess == random_number:
        print(f"congratulations! You gessed the number correctly in {guess} guesses")
        exit()
    elif guess < random_number:
        print("Your guess is too low")
    elif guess > random_number:
        print("Your guess is too high")

print(f"Sorry ! you couldn't guess the correct number!,correct number was {random_number}.")
    

    