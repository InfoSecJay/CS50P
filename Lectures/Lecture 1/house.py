name = input("Whats your name")

# if name == "Hary":
#     print("Gryffondor")
# elif name == "Hermonie":
#     print("Gryffondor")
# elif name == "Ron":
#     print("Gryffondor")
# elif name == "Ron":
#     print("Slytherin")
# elif name == "Hermonie":
#     print("Who?")


# if name == "Hary" or name == "Hermonie" or name == "Ron":
#     print("Gryffondor")
# elif name == "Ron":
#     print("Slytherin")
# elif name == "Hermonie":
#     print("Who?")


# can use mathc instead, but this regresses from before syntax....

""""match name:
    case "Harry":
        print("Gryffondor")
    case "Hermonie":
        print("Gryffondor")
    case "Ron":
        print("Gryffondor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")""""
        
        
match name:
    case "Harry" | "Hermoinie" | "Ron":
        print("Gryffondor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
        