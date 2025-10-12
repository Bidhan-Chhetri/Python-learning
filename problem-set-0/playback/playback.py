def main():
    text = str(input(""))
    playback(text)

def playback(get_text):
    print(get_text.replace(" ", "..."))

main()