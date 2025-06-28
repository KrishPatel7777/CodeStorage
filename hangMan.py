import random

words = ["shelf", "final", "index", "reach", "quota", "piece", "cater", "curve", "attic", "brain", "decay", "queen", "wrong", "lover", "trick", "tempt", "floor", "clear", "woman", "cause", "grass", "dough", "allow", "offer", "black", "harsh", "screw", "trial", "clash", "virus", "storm", "favor", "faith", "anger", "craft", "faint", "north", "solid", "trend", "panel", "habit", "begin", "tread", "match", "Koran", "moral", "prize", "lemon", "staff", "leash", "burst", "novel", "jewel", "bench", "lunch", "grave", "tempt", "embox", "rider", "amuse", "throw", "child", "forge", "clerk", "creed", "miner", "wrist", "ankle", "spine", "radio", "brave", "breed", "humor", "drain", "frank", "obese", "marsh", "dozen", "glare", "proof", "agree", "fight", "wheel", "steep", "board", "false", "slave", "story", "salon", "smash", "angel", "worry", "berry", "youth", "disco", "eagle", "lodge", "guess", "movie", "grand"]

random.shuffle(words)
word = random.choice(words).upper()
gLetters = []
lives = 7
cWord = ["_" for _ in word]

while lives > 0:
    print(f"\nLetters Guessed: {", ".join(gLetters)}")
    print(f"Current Word: {" ".join(cWord)}")
    print(f"Lives Left: {lives}")

    letter = input("Guess a Word: ").upper()

    if not letter.isalpha() or len(letter) != 1:
        print("⛔ Enter only a single letter.")
        continue

    if letter in gLetters:
        print("⚠️ Already guessed!")
        continue

    gLetters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                cWord[i] = letter

    else:
        lives-=1
        print("❌ Wrong guess!")

    if "_" not in cWord:
        print(f"\n✅ You WON! The word was: {word}")
        break

if "_" in cWord:
    print(f"\n💀 You LOST! The word was: {word}")