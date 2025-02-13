import random
import time

def main():
    print("*****************************************")
    print("Rock - Paper - Scissors")
    print("*****************************************")

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    while True:
        player = input("Enter your selection : ").lower()

        if not player in choices:
            print("Select a valid choice... ")
            time.sleep(1)
        else:
            if player == "rock" and computer == "scissors":
                print(f"Your Choice : {player.capitalize()}")
                print(f"Computer's Choice : {computer.capitalize()}")
                print("You Won !!!")
                time.sleep(1)

            elif player == "paper" and computer == " rock" :
                print(f"Your Choice : {player.capitalize()}")
                print(f"Computer's Choice : {computer.capitalize()}")
                print("You Won !!!")
                time.sleep(1)

            elif player == "scissors" and computer == "paper":
                print(f"Your Choice : {player.capitalize()}")
                print(f"Computer's Choice : {computer.capitalize()}")
                print("You Won")
                time.sleep(1)

            elif player == computer:
                print(f"Your Choice : {player.capitalize()}")
                print(f"Computer's Choice : {computer.capitalize()}")
                print("Draw")
                time.sleep(1)

            else:
                print(f"Your Choice : {player.capitalize()}")
                print(f"Computer's Choice : {computer.capitalize()}")
                print("You Lose")
                time.sleep(1)

        play_again = input("Wanna play again?\n"
                           "Y or N :").upper()
        if play_again == "Y":
            time.sleep(1)
            main()
        else:
            break

game = main()