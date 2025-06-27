import random
while True:
    while True:
        level = input("Enter Level: ")
        match level.lower():
            case "easy":
                range = 10
                lives = 2
                break
            case "medium":
                range = 50
                lives = 5
                break
            case "hard":
                range = 100
                lives = 10
                break
            case _:
                print("Invalid Level choose Easy, Medium or Hard")

    num = random.randint(1, range)
    print(num)
    print(f"Alright you have {lives} lives to guess the number between 1-{range}")
    gnum = 0
    while lives != 0:
        gnum = int(input(f"Lives: {lives} What's the Number? "))
        if gnum == num:
            print(f"Hooray the number was {num} and you won")
            break
        elif gnum != num:
            lives = lives - 1
            if lives == 0:
                print("You Lost")
            else:
                print("Try Again")
    if input("Wanna Play again(Yes/No) ? ").lower() == "yes":
        continue
    else:
        break