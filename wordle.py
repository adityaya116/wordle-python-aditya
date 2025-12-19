import random
five_letter_words = [
    "apple", "beach", "chair", "dance", "eagle", "fancy", "ghost", "house", "image", "juice",
    "knife", "lemon", "mouse", "night", "ocean", "piano", "queen", "radio", "snake", "tiger",
    "uncle", "voice", "water", "zebra", "bread", "cloud", "dream", "earth", "flame", "grape",
    "heart", "islnd", "jelly", "koala", "light", "melon", "nurse", "olive", "paper", "quiet",
    "river", "sheep", "table", "union", "video", "whale", "yeast", "acorn", "badge", "camel",
    "daisy", "elbow", "fairy", "giant", "heavy", "igloo", "joker", "kebab", "laser", "magic",
    "novel", "onion", "petal", "radar", "salad", "toast", "urban", "virus", "world", "yacht",
    "album", "bacon", "cabin", "daily", "early", "fable", "habit", "icing", "jewel", "kayak",
    "label", "mango", "noble", "opera", "panel", "quest", "robot", "sauce", "tempo", "unity",
    "value", "wagon", "xenon", "yield", "zones", "adore", "brave", "clean", "drive", "empty",
    "frost", "globe", "honey", "input", "joint", "knock", "level", "motor", "noise", "orbit"
]
word=random.choice(five_letter_words)
print("=====================")
print("    W O R D L E      ")
print("=====================")
print("_    _    _    _    _")


wordlst=list(map(str, word))
found_it=False
for turn in range(6):
    while True:
        tryy = input(f"try {turn+1}: ")
        if len(tryy) != 5:
            print("❌ Error: Word must be 5 letters long!")
            continue
        if not tryy.isalpha():
            print("❌ Error: Letters only please!")
            continue 
        break
    for i in range(5):
        print(f" {(tryy[i]).upper()}   ", end="")
    print()
    trylst=list(map(str, tryy))
    if word==tryy:
        print("🟩   🟩   🟩   🟩   🟩")
        print("found it!!")
        found_it=True
        break
    else:
        for i in range(5):
            if trylst[i]==wordlst[i]:
                print("🟩   ", end="")
            elif trylst[i] in wordlst:
                print("🟨   ", end="")
            else:
                print("⬛   ", end="")
        print()
if found_it==False:
    print(f"the word was : {word} \n better luck next time :)")