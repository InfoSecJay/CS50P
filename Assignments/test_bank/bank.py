def main():
    prompt = input("Greeting: ")
    print(value(prompt))


def value(greeting):
    greeting = greeting.lower()

    match greeting:
        case s if s.startswith("hello"):
            return "$0"
        case s if s.startswith("h"):
            return "$20"
        case _:
            return "$100"

if __name__ == "__main__":
    main()
