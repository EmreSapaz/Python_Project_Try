import time

print("****************************")
print("Welcome to the Python Quiz")
print("****************************\n")

play = input("Do you want to start?\n"
             "(Y or N):")

if play.upper() != "Y":
    ask_again = input("Are you sure?\n"
                      "(Y or N):")
    if ask_again.upper() != "N":
        print("So you choose quitting...\n"
         "Have a nice day!")
        quit()



questions = (("Which country commissioned the Statue of Liberty as a gift to the US"),
             ("How many ribs does a human skeleton have"),
             ("How many keys does have a piano"),
             ("The oldest person ever recorded lived to be what age"),
             ("Which is the largest continent in the world"))

options = (("A.England","B.France","C.Spain","D.Germany"),
          ("A.12","B.24","C.36","D.48"),
          ("A.80","B.84","C.88","D.92"),
          ("A.118","B.122","C.125","D.129"),
          ("A.Asia","B.Africa","C.Antartica","D.North America"))

answers = ("B","B","C","B","A")
question_no = 0
question_number = 1
Guesses = []
Score = 0

print("Quiz is been prepared...")
time.sleep(2)
for question in questions:
    print(f"----------------->Question {question_number}<-----------------")
    print(question)
    for option in options[question_no]:
        print(option)
    guess = input("Your Answer : ")
    time.sleep(.3)
    Guesses.append(guess.upper())
    if guess.upper() == answers[question_no]:
        Score += 1
    question_no += 1
    question_number += 1
print(f"Answers : {answers} ")
print(f"Your Guesses : {Guesses}")

print("******************************************")
print(f"Your Score : {Score*100/(question_number-1)}")
print("******************************************")


