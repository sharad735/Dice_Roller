import random
print("_______Welcome to the Game of roller dice________")
while(True):
    print("1.for roll the dice\n2.for exit the game")
    user = int(input("Enter the number of your choice: "))
    if user == 1:
        number = random.randint(1,6)
        print(f"Your number is {number}")
    else:
        break