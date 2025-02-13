from validator_collection import validators, checkers, errors

def main():
    print(check_email(input("Whats your email address? ")))

def check_email(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
