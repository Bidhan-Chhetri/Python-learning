import random

def main():
    count = 0
    input_level = get_level()

    for i in range(10):
        x, y = generate_integer(input_level)
        sum = x + y
        trys = 0
        while trys < 3:
            try:
                print(f"{x} + {y} = ", end="")
                get_sum = int(input())
                if sum == get_sum: 
                    count += 1
                    break
                else:
                    print("EEE")
                    trys += 1

            except ValueError:
                print("EEE")
                trys += 1


        if trys == 3:
            print(f"{x} + {y} = {sum}")
 
    print(f"Score = {count}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
       first_num = random.randint(1,9)
       second_num = random.randint(1,9)
       return first_num, second_num
    
    elif level == 2:
        first_num = random.randint(10,99)
        second_num = random.randint(10,99)
        return first_num, second_num
    
    elif level == 3:
        first_num = random.randint(100,999)
        second_num = random.randint(100,999)
        return first_num, second_num




if __name__ == "__main__":
    main()