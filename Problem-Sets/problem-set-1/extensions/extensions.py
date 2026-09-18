def main():
    prompt = str(input("File name: "))
    suffix = prompt.rsplit(".", 1)

    transform(suffix[1])

def transform(output):
    output = output.lower()
    if output in ["src", "jpg", "jpeg", "png", "pdf", "txt", "zip"]:
        print(f"image/" + output)

main()