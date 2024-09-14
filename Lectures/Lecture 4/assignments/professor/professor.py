import random



def main():
    level = get_level()
    x = generate_integer(level)
    y = generate_integer(level)
    print(x, "+", y)


    print()
    # level = get_level()
    # for i in range(q):
    #     new_question = generate_integer(level)
    #     print(new_question)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except ValueError:
            continue


def generate_integer(level):
    
    if level == 1:
        z = random.randrange(0,9)
    elif level == 2:
        z = random.randrange(10,99)
    else:
        z = random.randrange(100,999)
    return z

if __name__ == "__main__":
    main()