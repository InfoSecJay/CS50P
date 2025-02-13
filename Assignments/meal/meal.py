def main():
    user_input = input("What time is it? " )

    time = convert(user_input)

    if 7 <= time <= 8:
        return print("breakfast time")
    elif 12 <= time <= 13:
        return print("lunch time")
    elif 18 <= time <= 19:
        return print("dinner time")
    else:
        return False

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    float_time = hours + minutes
    return float_time


if __name__ == "__main__":
    main()
