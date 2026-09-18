import inflect

combine = []
while True: 
    try:
        name = input("Name: ")
        combine.append(name)
        
    except EOFError:
        print()
        print(f"Adieu, adieu, {inflect.engine().join(combine)}")
        exit()