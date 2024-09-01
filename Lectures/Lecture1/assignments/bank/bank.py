prompt = input("Greeting: ").lower()


match prompt:
    case s if s.startswith("hello"):
        print("$0")
    case s if s.startswith("h"):
        print("$20")
    case _:
        print("$100")