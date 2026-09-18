def main():
    question = str(input("What is the Answer to the Question of Life, the Universe, and Everything? ")) 
    question = " ".join(question.strip().lower().split())
    check(question)

def check(value):
    if value == "42" or value == 42 or value == "forty-two" or value == "forty two":
        print("yes")
    else:
        print("no")

main()