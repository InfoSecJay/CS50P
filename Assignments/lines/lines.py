import sys

def main():
    count = 0
    check_args()

    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if check_irrelevant_lines(line):
                    continue
                else:
                    count += 1
        print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_args():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

def check_irrelevant_lines(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()
