import random

choice =input("""
Welcome to temperature conveter !
pick an option
    1 - Celsius to Fahrenheit
    2 - Fahrenheit to Celsius
:""")

try:
    choice = int(choice)
except ValueError as error:
    print(f"please enter a vaild option")
    exit(1)
    
if choice == 1:
    celsius = input("Enter a temperature in celsius:")
    try:
        celsius = int(celsius)
    except ValueError as error:
        print(f"please enter a valid temperature!")
        exit(1)
    fahrenheit = (celsius*1.8)+32
    print(f"celsius {celsius} is equal to fahrenheit {fahrenheit}.")
elif choice == 2:
    fahrenheit = input("Enter a temperature in fahrenheit:")
    try:
        fahrenheit = int(fahrenheit)
    except ValueError as error:
        print(f"please enter a temperature!")
        exit(1)
    celsius = (fahrenheit-32)/1.8
    print(f"fahrenheit {fahrenheit} is equal to celsius {celsius}.")
else :
    print("invalid option entered !")    