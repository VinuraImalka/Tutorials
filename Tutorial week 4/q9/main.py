
repeat = True

while repeat:
    try:
        option = int(input("Select a menu option number:"))
    except ValueError:
        print("Please select a vaild menu option number")
        continue
    if option == 1:
        print("1 selected")
    elif option == 2:
        print("2 selected")
    elif option == 3:
        print("3 selected")
    elif option == 4:
        print("Quit selected")
        exit()
    else:
        print("Option not recognised")