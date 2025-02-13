from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
        print(time_delta(input("Date: ")))

def time_delta(birth_date):

    try:
        year, month, day = birth_date.split("-")
        birth_date = date(int(year), int(month), int(day))
    except:
        return sys.exit("Invalid date")

    time_delta =  date.today() - birth_date
    total_minutes = time_delta.days * 24 * 60
    song = p.number_to_words(total_minutes, andword="")
    return song.capitalize() + " minutes"

if __name__ == "__main__":
    main()
