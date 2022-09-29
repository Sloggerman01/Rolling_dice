import random

response = input("Do you want to Roll the dice?")
while response == "y":
    number = random.randint(1, 6)
    if(number == 1):
        print("[-----]", end="\n")
        print("[-----]", end="\n")
        print("[  0  ]", end="\n")
        print("[-----]", end="\n")
        print("[-----]", end="\n")
        response = input("Do you want to roll again")
    if(number == 2):
        print("[-----]", end="\n")
        print("[0    ]", end="\n")
        print("[     ]", end="\n")
        print("[    0]", end="\n")
        print("[-----]", end="\n")
        response = input("Do you want to roll again")
    if(number == 3):
        print("[-----]", end="\n")
        print("[-----]", end="\n")
        print("[0 0 0]", end="\n")
        print("[-----]", end="\n")
        print("[-----]", end="\n")
        response = input("Do you want to roll again")
    if(number == 4):
        print("[0   0]", end="\n")
        print("[     ]", end="\n")
        print("[     ]", end="\n")
        print("[     ]", end="\n")
        print("[0   0]", end="\n")

    if(number == 5):
        print("[0   0]", end="\n")
        print("[     ]", end="\n")
        print("[  0  ]", end="\n")
        print("[     ]", end="\n")
        print("[0   0]", end="\n")
