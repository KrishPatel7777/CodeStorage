import random
while True:
    choice = ["r", "p", "s"]
    comDec = random.choice(choice)

    while True:
        userDec = input("Rock, Paper or Scissor: ").strip().lower()
        if userDec == "rock" or userDec == "paper" or userDec == "scissor":
            break
        else:
            print("Invalid!") 
            continue
        
    if userDec == "rock":
        if comDec == "p":
            print("User Lost")
        elif comDec == "s":
            print("User Won")
        else:
            print("Draw")
    elif userDec == "paper":
        if comDec == "s":
            print("User Lost")
        elif comDec == "r":
            print("User Won")
        else:
            print("Draw")
    else:
        if comDec == "r":
            print("User Lost")
        elif comDec == "p":
            print("User Won")
        else:
            print("Draw")
    if input("Wanna Play again(Yes/No) ? ").lower() == "yes":
        continue
    else:
        break