import random

ROCK = "r"
SCISSOR = "s"
PAPER = "p"
emojies = {"r": "🪨", "p" : "📃", "s" : "✂️"}
option = tuple(emojies.keys())

def main():
    answer = choosing()
    computer_choice = display_choices()
    determine_winner(answer, computer_choice)
    check_continue = input("Continue (y/n): ")
    if check_continue == "y":
        main()
            


def choosing():
    while True:
        answer = str(input("Rock, paper or scissor? (r/p/s): ")).lower()

        if answer in option:
            print(f"you Choose {emojies[answer]}")
            break
        else:
            print("Enter the valid integer")
    return answer

def display_choices():
        computer = random.choice(option)
        print(f"Computer choose {emojies[computer]}")
        return computer

def determine_winner(answer, computer):      
        if answer == ROCK:
            if computer == ROCK:
                print("Tie")
            elif computer == PAPER:
                print("Computer wins")
            else:
                print("I win")
        elif answer == "s":
            if computer == "s":
                print("Tie")
            elif computer == ROCK:
                print("Computer wins")
            else:
                print("I win")
        elif answer == PAPER:
            if computer == PAPER:
                print("Tie")
            elif computer == ROCK:
                print("Computer wins!")
            else:
                print("I win")

main()
