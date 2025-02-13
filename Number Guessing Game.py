import random

min_number = input("Starting point : ")
max_number = input("Ending point : ")

while min_number > max_number:
    print("Starting point cannot be smaller than ending point")
    min_number = input("Starting point : ")
    max_number = input("Ending point : ")

while not min_number.isdigit() or not max_number.isdigit():
    print("Please enter a number")
    min_number = input("Starting point : ")
    max_number = input("Ending point : ")

min_number = int(min_number)
max_number = int(max_number)

random_number = random.randint(min_number,max_number)

guess_number = 0

while True:
    guess = input("Your Guess : ")

    if not guess.isdigit():
        print("Your guess must be a number")
        guess = input("Your Guess : ")
        continue

    guess = int(guess)

    if guess < 0:
        print("Your guess cannot be smaller than 0")
        guess = input("Your Guess : ")
        continue

    if not max_number >= guess >= min_number:
        print("Your guess must be between starting end ending points")
        guess = input("Your Guess : ")
        continue

    if guess > random_number:
        print("Select a smaller number")
        guess_number += 1

    elif guess < random_number:
        print("Select a bigger number")
        guess_number += 1

    else:
        print("You Won!!!")
        print(f"Total Guess : {guess_number}")