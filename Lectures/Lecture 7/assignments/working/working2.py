import re


def main():
    print(convert(input("Hours: ")))

def convert(s):
    
    pattern = r"^(([0-9][0-2]*):?([0-5][0-9])*) (AM|PM) to (([0-9][0-2]*):?([0-5][0-9])*) (AM|PM)$"
    
    if matches := re.search(pattern, s, re.IGNORECASE):
        parts = matches.groups()
        if int(parts[1]) > 12 or int(parts[5]) > 12 or int(parts[2]) > 59 or int(parts[6]) > 59:
            raise ValueError
        first_time = new_format(parts[1], parts[2], parts[3])
        second_time = new_format(parts[5], parts[6], parts[7])
        return first_time + " to " + second_time
    else:
        raise ValueError
        
def new_format(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
            
    if minute == None:
        new_minute = ':00'
        new_time = new_hour + new_minute
    else:
        new_time = f"{new_hour:02}" + ":" + minute
        
    return new_time

if __name__ == "__main__":
    main()