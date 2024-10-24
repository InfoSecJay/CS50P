import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(([0-9][0-2]*):?([0-5][0-9])*) (AM|PM) to (([0-9][0-2]*):?([0-5][0-9])*) (AM|PM)$", s, re.IGNORECASE):
        pieces = matches.groups()
        print(pieces)


if __name__ == "__main__":
    main()