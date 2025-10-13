def main():
    greeting = str(input("Greeting: "))
    greeting = greeting.lower().strip()
    check(greeting)

def check(string):
    if string[:5] == 'hello':
        print("$0")
    elif string[0:1] == 'h' and string[0:5] != 'hello':
        print("$20")
    else:
        print("$100")

main()