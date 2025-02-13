
def main():

    while True:
        try:
            user_input = int(input("Height: "))
            if user_input < 1 or user_input > 8:
                continue  # Prompt again if out of range
        except ValueError:
            continue

        print_row(user_input)
        exit()

def print_row(height):

    for i in range(height):
        print(" " * (height - i - 1), end="")
        print("#" + "#"* i, end="")
        print("  ", end="")
        print("#" + "#"* i)

if __name__ == "__main__":
    main()
