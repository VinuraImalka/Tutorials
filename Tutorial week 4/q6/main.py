try:    
    num = int(input("Enter number of stars:"))
    for i in range (num):
        print("*",end="")
except ValueError:
    print("Please enter vaild number")


    