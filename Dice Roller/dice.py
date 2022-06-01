import random
x = 'y'
while x == 'y':
    num = random.randint(1,6)
    if num == 1:
        print("[-----]")
        print("[     ]")
        print("[  1  ]")
        print("[     ]")
        print("[-----]")
    if num == 2:
        print("[-----]")
        print("[2    ]")
        print("[     ]")
        print("[    2]")
        print("[-----]")
    if num == 3:
        print("[-----]")
        print("[     ]")
        print("[ 333 ]")
        print("[     ]")
        print("[-----]")
    if num == 4:
        print("[-----]")
        print("[4   4]")
        print("[     ]")
        print("[4   4]")
        print("[-----]")
    if num == 5:
        print("[-----]")
        print("[5   5]")
        print("[  5  ]")
        print("[5   5]")
        print("[-----]")
    if num == 6:
        print("[-----]")
        print("[6 6 6]")
        print("[     ]")
        print("[6 6 6]")
        print("[-----]")
    x = input("Press y to roll again & n to exit: ")
    print("\n")