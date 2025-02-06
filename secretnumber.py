import random

def secret_number():
    return random.randint(1, 10)

while True:
    guess = int(input("Guess the secret number between 1 and 10: "))
    if guess == secret_number():
        print(f"You are correct! The secret number is {guess}")
        break
    else:
        print("Wrong, try again!")