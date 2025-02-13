import random

def main():


    level = get_level()

    q = 10

    score = 0

    for i in range(q):
        x = generate_integer(level)
        y = generate_integer(level)
        actual_ans = x + y
        fail_count = 0

        while True:

            try:
                user_ans = int(input(f"{x} + {y} = "))

                if user_ans == actual_ans:
                    score += 1
                    break
                else:
                    fail_count += 1
                    print("EEE")
                    if fail_count == 3:
                        print(f"{x} + {y} = {actual_ans}")
                        break
                    continue
            except ValueError:
                print("EEE")
                fail_count += 1
                if fail_count == 3:
                    print(f"{x} + {y} = {actual_ans}")
                    break

    print("Score: ", score)


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
        z = random.randint(0,9)
    elif level == 2:
        z = random.randint(10,99)
    else:
        z = random.randint(100,999)
    return z

if __name__ == "__main__":
    main()
