import re


AMEX = r"^(34|37)\d{13}"
MASTERCARD = r"^(51|52|53|54|55)\d{14}"
VISA = r"^4\d{12}(\d{3})?$"

def main():
    user_input = input("Number: ")

    if calculate_checksum(user_input):
        print(check_vendor(user_input))
    else:
        print("INVALID\n")

def calculate_checksum(user_input):

    x = int(user_input)
    total, sum1, sum2, mod1, mod2, d1, d2 = 0, 0, 0, 0, 0, 0, 0

    while x > 0:
        mod1 = x % 10
        x = x // 10
        sum1 += mod1

        mod2 = x % 10
        x = x // 10

        mod2 *= 2
        d1 = mod2 % 10
        d2 = mod2 // 10
        sum2 += d1 + d2

    total = sum1 + sum2

    return total % 10 == 0


def check_vendor(user_input):

    length = len(user_input)

    if length not in (13, 15, 16):
        return "INVALID\n"
    if re.match(AMEX, user_input):
        return "AMEX\n"
    elif re.match(MASTERCARD, user_input):
        return "MASTERCARD\n"
    elif re.match(VISA, user_input):
        return "VISA\n"
    else:
        return "INVALID\n"

if __name__ == "__main__":
    main()


