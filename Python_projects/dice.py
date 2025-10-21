import random

def main():
    while True:
        choice = input("Roll the dice(y/n): ")
        if choice in ["y", "Y"]:
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print(f"({die1}, {die2})")
        elif choice in ["n", "N"]:
            print("Thanks for plying")
            break
        else:
            print("Invalid choice")


main()