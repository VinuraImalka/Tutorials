""" age = int(input("Enter your age"))
if age >= 18:
    print("Can vote")
else:
    print("Can't vote") """
    
age = input("what is your age?:")
try:
    age = int(age)
    if age >= 18:
        print("Can vote")
    else:
        print("Can't vote")
except ValueError as error:
    print(f"you can't use '{age}' as your age")        

