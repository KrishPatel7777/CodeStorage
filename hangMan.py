import random

words = ["maniacal", "breath", "toothpaste", "satisfying", "treat", "horse", "lovely", "ruddy", "wretched", "allow", "alert", "rabid", "undress", "messy", "wood", "reading", "finger", "awesome", "mysterious", "prick", "wheel", "rejoice", "succinct", "temper", "aboard", "smoke", "excellent", "scatter", "disgusting", "enjoy", "draconian", "uttermost", "analyze", "plant", "abject", "receptive", "material", "hanging", "chance", "interest", "flock", "coil", "anger", "amount", "sleep", "flowers", "nail", "wool", "minister", "spiritual", "desert", "handsomely", "hallowed", "exercise", "delirious", "laborer", "nifty", "fearful", "rampant", "giraffe", "industry", "tasteless", "kneel", "spoil", "jealous", "inexpensive", "wound", "efficacious", "previous", "reproduce", "stereotyped", "table", "mask", "farm", "jail", "bear", "pull", "devilish", "improve", "successful", "dance", "appreciate", "committee", "tickle", "utter", "sponge", "subsequent", "stomach", "grade", "combative", "pointless", "grateful", "division", "chase", "innate", "camera", "book", "average", "abounding", "experience", "ludicrous", "suspect", "credit", "front", "close", "unnatural", "uptight", "makeshift", "salt", "tacit", "confess", "quarter", "wrench", "suggest", "middle", "busy", "supply", "parched", "observation", "store", "shave", "better", "deserve", "airplane", "suffer", "cluttered", "turkey", "frantic", "crooked", "nutritious", "adamant", "battle", "branch", "willing", "jagged", "boiling", "special", "blood", "faulty", "shaky", "hospitable", "ignore", "sweet", "hissing", "rustic", "multiply", "hushed", "seashore", "humorous", "futuristic", "tremendous", "ratty", "wander", "chickens", "sudden", "unable", "afford", "receive", "erratic", "signal", "building", "paddle", "tearful", "communicate", "enchanting", "treatment", "animated", "bless", "stretch", "endurable", "disapprove", "writing", "button", "fertile", "learned", "holiday", "omniscient", "painstaking", "preach", "nebulous", "doubt", "fallacious", "abundant", "wall", "army", "iron", "material", "bolt", "remind", "efficient", "outstanding", "wheel", "picayune", "society", "harmonious", "humdrum", "quizzical", "rebel", "jellyfish", "develop", "unite", "quartz", "unknown", "glossy", "position", "uninterested", "ritzy", "divide", "thoughtless", "scarecrow", "poison", "shiver", "worry", "ticket", "announce", "cagey", "elastic", "cross", "swift", "idiotic", "historical", "silver", "mailbox", "gold", "glow", "defeated", "flood", "rainstorm", "profuse", "harmony", "apparatus", "float", "behavior", "jumpy", "basin", "snake", "economic", "belligerent", "yellow", "earthquake", "plants", "silky", "locket", "abrupt", "oranges", "agreement", "wealthy", "badge", "kindly", "aggressive", "picture", "magic", "table", "connection", "gruesome", "moan", "songs", "judicious", "change", "cough", "building", "steer", "scissors", "fanatical", "hammer", "unwritten", "gusty", "rake", "shaky", "bridge", "distribution", "flash", "drip", "broken", "homely", "hateful", "brass", "common", "crown", "needless", "history", "foregoing", "shape", "gorgeous", "acrid", "mug", "gaudy", "ceaseless", "steady", "twist", "flippant", "typical", "cattle", "absurd", "discussion", "cheerful", "tramp", "grumpy", "trade", "stupendous", "reflect", "wave", "psychotic", "bouncy", "record", "order", "wheel", "secretary", "selective", "park", "dress", "transport", "thunder", "bells", "famous", "observation", "riddle", "level", "greedy", "chalk", "market", "bawdy", "miscreant"]

random.shuffle(words)
word = random.choice(words).upper()
gLetters = []
lives = 10
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