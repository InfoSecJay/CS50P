def main():
    expression = input("Expression: ")
    return interpreter(expression)

def interpreter(input):
    x, y, z = input.split(" ")
    x = float(x)
    z = float(z)

    if y == "+":
        return print(x + z)
    elif y == "-":
        return print(x - z)
    elif y == "*":
        return print(x * z)
    elif y == "/":
        return print(round(x / z, 1))
    else:
        return print("Not a valid operator, try again!")

main()
