import random
moves = ["X", "O"]
tiles = [
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " "
]
win = ""

while win != "user" and win != "computer":
    comChoice = random.randint(0, 8)
    if tiles[comChoice] == "X" or tiles[comChoice] == "O":
        comChoice = random.randint(0, 8)
        continue
    tiles[comChoice] = "X"
    if tiles[0] == tiles[1] == tiles[2] == "X" or tiles[3] == tiles[4] == tiles[5] == "X" or tiles[6] == tiles[7] == tiles[8] == "X":
        win = "computer"
    elif tiles[0] == tiles[3] == tiles[6] == "X" or tiles[1] == tiles[4] == tiles[7]== "X" or tiles[2] == tiles[5] == tiles[8]== "X":
         win = "computer"
    elif tiles[0] == tiles[4] == tiles[8] == "X" or tiles[2] == tiles[4] == tiles[6] == "X":
        win = "computer"
    while True:
        try:
            userChoice = int(input("User's Turn(0-8): "))
            if userChoice > 8:
                print("Choice should between 0-8")
            elif tiles[userChoice] == 'X' or tiles[userChoice] == "O":
                print("Already Taken!!")
                continue
            else:
                tiles[userChoice] = "O"
                break
        except ValueError:
            print("Choice should be integer!!")
            continue

    if tiles[0] == tiles[1] == tiles[2] == "O" or tiles[3] == tiles[4] == tiles[5] == "O" or tiles[6] == tiles[7] == tiles[8] == "O":
        win = "user"
    elif tiles[0] == tiles[3] == tiles[6] == "O" or tiles[1] == tiles[4] == tiles[7]== "O" or tiles[2] == tiles[5] == tiles[8]== "O":
        win = "user"
    elif tiles[0] == tiles[4] == tiles[8] == "O" or tiles[2] == tiles[4] == tiles[6] == "O":
        win = "user"
    print(f"\n{tiles[0]} | {tiles[1]} | {tiles[2]}")
    print(f"{tiles[3]} | {tiles[4]} | {tiles[5]}")
    print(f"{tiles[6]} | {tiles[7]} | {tiles[8]}\n")
    print(f"Computer ticked in square {comChoice}\n")

print(f"{win.upper()} Won!!")