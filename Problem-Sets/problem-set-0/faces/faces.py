def main():
    faces = str(input(""))
    change(faces)

def change(to):
    print(to.replace(":)", "🙂").replace(":(", "🙁"))

main()

