def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    plates = s.lower()
    if plates[0:2].isalpha() and len(plates) <= 6 and plates[-1].isnumeric() and len(plates) >= 2 and plates.isalnum():
            for word in range(len(plates)):
                if plates[word].isdigit():
                    if plates[word] == '0':
                         break
                    return True
    else:
        return False


main()
