def parse_int(s: str):
    try:
        parsed_int = int(s)
    except ValueError:
        return None
    except TypeError:
        return None
        
    return parsed_int
    
def get_num_from_user():
    user_input = input ("Enter number or type -9 to quit:")
    parsed_int = parse_int(user_input)
    
    if parsed_int is None:
        print("please enter num again !")
        return get_num_from_user()
    
    return parsed_int

total , count = 0, 0
parsed_user_input = get_num_from_user()

while parsed_user_input != -9:
    total += parsed_user_input
    count += 1
    parsed_user_input = get_num_from_user()
    
print(f"total:{total}")
print(f"count:{count}")
