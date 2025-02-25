import random

choices = ['rock', 'paper', 'scissors']

while True:
    x = input("What do you want to play with?: ")
    computer = random.choice(choices)

    if x == 'rock' and computer == 'rock':
        print("You choose the same option as the AI, you thus do a draw")
    elif x == 'rock' and computer == 'paper':
        print("You lost")
    elif x == 'rock' and computer == 'scissors':
        print("You won")
    elif x == 'paper' and computer == 'rock':
        print("You Won")
    elif x == 'paper' and computer == 'paper':
        print("You choose the same option as the AI, you thus make a draw")
    elif x == 'paper' and computer == 'scissors':
        print("You lost")
    elif x == 'scissors' and computer == 'scissors':
        print("You choose the same option as the AI, you thus do a draw")
    elif x == 'scissors' and computer == 'rock':
        print("You lost")
    elif x == 'scissors' and computer == 'paper':
        print("You won")
    else:
        print("Invalid choice, try again!")
        continue

    y = input("To continue, press Enter. To exit, type 'exit': ").lower()
    if y == 'exit':
        exit()
    else:
        continue
