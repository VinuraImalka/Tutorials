import random
double = 0
for i in range(100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1 == dice2:
        double = double +1
print(f"Out of 100 you rolled {double} doubles")        