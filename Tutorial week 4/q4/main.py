sum = 0


for i in range (5):
    is_number = True
    while is_number:
        try:
            num = int(input("Enter a number:"))
            sum = sum + num          
            is_number = False   
        except ValueError:
            print("Please enter a number")
    
print(f"Total is {sum}")
    