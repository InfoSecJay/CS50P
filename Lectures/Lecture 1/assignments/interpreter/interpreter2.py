def main():
    expression = input("Expression: ")
    return interpreter(expression)

def interpreter(x):
    x, y, z = x.split(" ")
    x = float(x)
    z = float(z)

    match y:
        case y if y == "+":
            return print(x + z)
        case y if y == "-":
            return print(x - z)
        case y if y == "*":
            return print(x * z)
        case y if y == "/":
            return print(x / z)
        case _:
            return print("Not a valid operator, try again!")
        
main()