import random
def guessingGame(guessed_number, random_number):
    total_points = 100
    random.randint(1,100)
    while guessed_number != random_number:
        if guessed_number == random_number:
            break
        total_points -= 1
        if guessed_number > random_number:
            print("Too high!")
        elif guessed_number < random_number:
            print("Too low!")
    return f"Bingo! Your total points is {total_points}"

try:
    print(guessingGame(guessed_number = int(input("Guess the number: ")), random.randint(1,100)))
except ValueError:
    print("Input Error! Try again!")
