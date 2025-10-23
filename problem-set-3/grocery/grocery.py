def main():
    total = []
    count = 1
    while True:
        try:
            item = input("").upper()
            total.append(item)
        except EOFError:
            for item in total:
                print(count, item)
                count = count + 1
            break


main()