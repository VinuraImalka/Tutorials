sum = 0

print("""         Welcome To calculator!
         First enter a number, 
         Then enter a operator(+,-,/,*),
         Lastly enter a second number.
      """)
try:
    num1 = int(input("Enter the first number:"))
except ValueError as error:
    print(f"please enter vaild number!")
    exit()
    
operator = input("Enter the operator:")

try:
    num2 = int(input("Enter the second number:"))
except ValueError as error:
    print(f"please enter vaild number!")
    exit()    

try:
    if operator == "+":
        sum = num1 + num2
        print(f"{num1}{operator}{num2}={sum}")
        exit()
        
    elif operator == "-":
        sum = num1 - num2
        print(f"{num1}{operator}{num2}={sum}")
        exit() 
        
    elif operator == "/":
        sum = num1 / num2
        print(f"{num1}{operator}{num2}={sum}")
        exit()
        
    elif operator == "*":
        sum = num1 * num2
        print(f"{num1}{operator}{num2}={sum}")
        exit()
    else:
        print(f"{operator} is not a vaild option!")
        exit()
except ZeroDivisionError as error:
    print("Number cannot be divided by zero!")
    