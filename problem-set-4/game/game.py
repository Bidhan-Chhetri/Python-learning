import random

while True:
    try:
        get_level = int(input("Level: "))
        if get_level < 1:
            continue
        break
    except ValueError:
        continue

get_random = random.randint(1, get_level) 

while True: 
    try:
        get_guess = int(input("Guess: "))
        if get_guess == get_random:
            print("Just right")
            exit()
        elif get_guess > get_random:
            print("Too large")
        elif get_guess < get_random:
            print("Too small")
    except ValueError:
        pass

        