from datetime import date, datetime
import re
import sys
import inflect

p = inflect.engine()
current_date = datetime.today()


def main():
    user_input = input("Date of Birth: ")
    minutes = time_delta(user_input)
    print(number_to_words(minutes))

def time_delta(birth_date):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if matches := re.search(pattern, birth_date):
        try:
            birth_date = datetime.strptime(birth_date, "%Y-%m-%d").replace(hour=0, minute=0, second=0, microsecond=0)
            interval = current_date - birth_date
            total_minutes = round(interval.total_seconds() / 60)
            return total_minutesa
        except ValueError:
            sys.exit("Not a valid date")
    else:
        sys.exit("Not YYYY-MM-DD format")
    


def number_to_words(total_minutes):
    song = p.number_to_words(total_minutes)
    return f"{song.capitalize().replace(" and", ",")} minutes"
    
if __name__ == "__main__":
    main()