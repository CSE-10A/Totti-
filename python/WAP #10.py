import random

number = random.randint(1, 9)

guess = ()

while guess != number:
    guess = int(input("Wrong guess, try again: "))
    
print("Well guessed!")