try:
    cost = int(input("Please enter the cost of the meal :"))
except ValueError as error:
    print(f"please enter the correct cost!")
    exit()
    
satisfaction = input("""Please select your satisfaction level using ratings,
        1 = Totally satisfied, 
        2 = Satisfied, 
        3 = Dissatisfied.
:""")
print("------------------------------------------------")
if satisfaction == '1':
    tip = cost * 0.20
elif satisfaction == '2':
    tip = cost * 0.15
elif satisfaction == '3':
    tip = cost * 0.10
else:
    print("please enter a vaild option!")
    exit()
print(f"Tip is {tip}")