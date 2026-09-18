def main():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x > y:
                continue
            percentage = round((x / y) * 100)
            break
        except ZeroDivisionError:
            percentage = 0
            break
        except ValueError:
            print(f"Give an integer")
            continue
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")
    

main()