def main():
    question = 50
    while question > 0:
        print(f"Amount Due: {question}")
        insert = int(input("Insert coin: "))
        if insert in [25, 10, 5]:
           question = question - insert
        if question <= 0:
            continue
    print(f"Changed Owed {-question}")

main()