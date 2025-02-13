import random

lose_number = int(input("Choose a number between 1-6:"))

dice_art ={
    1:("┌──────────┐",
       "│          │",
       "│    ●     │",
       "│          │",
       "└──────────┘"),


    2:("┌──────────┐",
       "│  ●       │",
       "│          │",
       "│       ●  │",
       "└──────────┘"),


    3:("┌──────────┐",
       "│  ●       │",
       "│     ●    │",
       "│        ● │",
       "└──────────┘"),


    4:("┌──────────┐",
       "│  ●     ● │",
       "│          │",
       "│  ●     ● │",
       "└──────────┘"),


    5:("┌──────────┐",
       "│  ●     ● │",
       "│     ●    │",
       "│  ●     ● │",
       "└──────────┘"),


    6:("┌──────────┐",
       "│  ●     ● │",
       "│  ●     ● │",
       "│  ●     ● │",
       "└──────────┘"),

}

def main():
    score: int = 0
    while True:
        roll = random.randint(1,6)
        print("You rolled...\n")
        for line in range(5):
            print(dice_art.get(roll)[line])

        if roll == lose_number:
            print(f"Your Score : {score}")
            print("You Lose!!")
            break

        else:
            score += roll
            print(f"Your current score : {score}")
            again = input("Wanna roll again?\nY or N:").lower()

            if again != "y":
                print(f"Your Score : {score}")
                break

main()