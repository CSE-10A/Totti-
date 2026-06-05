import random

num1 = ()
num2 = ()

multiplication = (num1 * num2)
division = (num1/num2) 
addition = (num1 + num2)
subtraction = (num1 - num2) 
modulus = (num1 % num2)
 
operation = (multiplication, division, addition, subtraction, modulus)

operation = random.choice(operation)

if operation == multiplication:
    print(multiplication)

elif operation == division:
    if num2 == 0:
        print("Cant divide by 0") 
    else:
        print(division)

elif operation == addition:
    print(addition)

elif operation == subtraction:
    print(subtraction)

elif operation == modulus:
    print(modulus)
