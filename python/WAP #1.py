import random
character = ("c")
    
vowel = ["a", "e", "i", "o", "u", "y"]

# pick a random character
character = random.choice(character)

if character in vowel:
    print("Vowel")
else: 
    print("Not a Vowel")
