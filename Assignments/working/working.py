import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^([0-9]{1,2})(?::([0-5][0-9]))? (AM|PM) to ([0-9]{1,2})(?::([0-5][0-9]))? (AM|PM)$"

    if matches := re.match(pattern, s, re.IGNORECASE):
        first_hour, first_minute, first_ampm, second_hour, second_minute, second_ampm = matches.groups()
        first_time = new_format(int(first_hour), first_minute or "00", first_ampm)
        second_time = new_format(int(second_hour), second_minute or "00", second_ampm)
        return f"{first_time} to {second_time}"
    else:
        raise ValueError("Invalid time format")

def new_format(hour, minute, ampm):
    if ampm == "PM" and hour != 12:
        hour += 12
    elif ampm == "AM" and hour == 12:
        hour = 0
    return f"{hour:02}:{minute}"

if __name__ == "__main__":
    main()
