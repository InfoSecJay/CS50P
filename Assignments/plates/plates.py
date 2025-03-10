"""
In plates.py, implement a program that prompts the user for a vanity plate and then output
Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in
the user’s input will be uppercase. Structure your program per the below, wherein is_valid
returns True if s meets all requirements and False if it does not. Assume that s will be a str.
You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
"""

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):

    if plate.isalnum() and plate[0:1].isalpha() and 2 <= len(plate) <= 6:
        for item in plate:
            if item.isdigit():
                index = plate.index(item)
                if plate[index:].isdigit() and int(item) != 0:
                    return True
                else:
                    return False
        return True

if __name__ == "__main__":
    main()
