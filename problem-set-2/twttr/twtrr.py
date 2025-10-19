def main():
    word = str(input("Input: "))
    check(word)

def check(word):
    lower = word.lower()
    print("hello!, World")
    for i in lower:
        if i not in ('a', 'e', 'i', '0', 'u'):
            print(i, end = "")
    

main()