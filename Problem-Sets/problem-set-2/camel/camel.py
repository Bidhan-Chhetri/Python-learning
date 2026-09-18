def main():
    word = str(input("camelCase: "))
    word_list = list(word)
    snake_case(word_list)

def snake_case(word_list):
    list = []
    for i in range(len(word_list)):
        if word_list[i].isupper():
            list.append("_")
            list.append(word_list[i].lower())
        else:
            list.append(word_list[i])

    change_to_string(list)

def change_to_string(word_list):
    word =[""]
    for word in word_list:
        print(word, end = "")
main()