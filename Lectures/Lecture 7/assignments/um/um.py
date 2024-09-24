import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    pattern = '\\bum\\b'
    count = 0
    for match in re.finditer(pattern, s, re.IGNORECASE):
        count += 1
    return count

if __name__ == "__main__":
    main()