import random

def main():
    
    computer = random.choice(["rock", "paper", "scissor"])
    while True:
        answer = str(input("Rock, paper or scissor? (r/p/s): ")).lower()
        if answer == "r":
            if computer == "rock" or computer == "r":
                print("Tie")
            elif computer == "paper" or computer == "p":
                print("Computer wins")
            else:
                print("I win")
        elif answer == "s":
            if computer == "scissor" or computer == "s":
                print("Tie")
            elif computer == "rock" or computer == "r":
                print("Computer wins")
            else:
                print("I win")
        elif answer == "p":
            if computer == "paper" or computer == "p":
                print("Tie")
            elif computer == "rock" or computer == "r":
                print("Computer wins!")
            else:
                print("I win")
        elif answer in ["r", "p", "s"]:
            print("Enter the valid integer")
            continue
        print(f"Computer choose {computer}")
        
        choose = str(input("Continue (y/n): ")).lower()
        if choose == "y":
            continue
        else:
            break
main()