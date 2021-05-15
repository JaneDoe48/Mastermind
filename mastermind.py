import random

NUMBER_TO_GUESS = random.randrange(100,109)  

NB_ROUNDS = int(input("How many tries do you want?"))
input_num = int(input("Guess the number:"))

if (input_num == (NUMBER_TO_GUESS%10)):  
    print("Great! You guessed the number in just one try! You're a Mastermind!")
else:
    number = NUMBER_TO_GUESS%10
    for i in range(1, NB_ROUNDS):
        if (input_num != number):
            input_num = int(input("Try again..."))
        else:
            print("You won!")
            break