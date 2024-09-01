def main():
    user_input = input("What time is it? " )
    
    time = convert(user_input)
    
    if 7 <= time <= 8:                  # breakfast is between 7 and 8...
        return print("breakfast time")
    elif 12 <= time <= 13:
        return print("lunch time")
    elif 18 <= time <= 19:
        return print("dinner time")
    else:
        return False

def convert(time):
    hours, minutes = time.split(":")   # split the user input by ":" into hours and minutes
    hours = float(hours)               # set the hours to float
    minutes = float(minutes) / 60      # divide minutes by 60 to get the float representation of the time
    float_time = hours + minutes       # combine the values to form the "new float time"
    return float_time                  # satisfy the condition where convert must convert time, a str in 24hr format, to corresponding hours as float
    

if __name__ == "__main__":
    main()