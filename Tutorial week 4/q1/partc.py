import random

hidden =6 
is_matched = False

random_num = random.randint(1,20)

while(not is_matched):
    is_matched = random_num == hidden
    if is_matched:
        print(f"{random_num} is the correct number")
    else :
        print(f"{random_num} is not the correct number")
        random_num = random.randint(1,20)

