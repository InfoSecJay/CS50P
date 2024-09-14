"""
In a file called outdated.py, implement a program that prompts the user for a date,
anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
wherein the month in the latter might be any of the values in the list below:[dict]

Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid
date in either format, prompt the user again. Assume that every month has no more
than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

dict = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:

        date = input("Date: ")

        if "/" in date:
            month, day, year = date.split("/")

        elif "," in date:
            date = date.replace(",", "")
            month, day, year = date.split(" ")
            if month in dict:
                month = dict.index(month) + 1
                
        else:
            continue

        try:
            if int(month) > 12 or int(day) > 31:
                continue
            else:
                break
        except ValueError:
            continue

    print(f"{int(year)}-{int(month):02}-{int(day):02}" )

if __name__ == "__main__":
    main()
