def main(): 
    expression = str(input("Expression: "))
    x, y, z = expression.split(" ")
    print(x, y,z)

    x = int(x)
    z = int(z)

    if y == "+":
        print(float(x + z))
    elif  y == "/":
        print(float(x / z))
    elif y == "-":
        print(float(x - z))
    elif y == "*":
        print(float(x * z))
    

main()

