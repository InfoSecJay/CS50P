from cs50 import get_float

def main():

    while True:
        try:
            user_input = get_float("Change: ")
            if user_input < 0:
                print("Please enter a non-negative value.")
                continue  # Ask the user again if the input is negative
        except ValueError:
            print("Please enter numeric values.")
            continue # Ask the user again if the input gives a value error (string)
        break

    cents = round(user_input * 100)

    quarters = calculate_quarters(cents)
    cents = cents - (quarters * 25)

    dimes = calculate_dimes(cents)
    cents = cents - (dimes * 10)

    nickels = calculate_nickels(cents)
    cents = cents - (nickels * 5)

    pennies = calculate_pennies(cents)
    cents = cents - (pennies * 1)

    sum = quarters + dimes + nickels + pennies
    print(sum)

def calculate_quarters(coins):
    quarters = 0
    while (coins >= 25):
        quarters += 1
        coins = coins - 25
    return quarters

def calculate_dimes(coins):
    dimes = 0
    while (coins >= 10):
        dimes += 1
        coins = coins - 10
    return dimes

def calculate_nickels(coins):
    nickels = 0
    while (coins >= 5):
        nickels += 1
        coins = coins - 5
    return nickels

def calculate_pennies(coins):
    pennies = 0
    while (coins >= 1):
        pennies += 1
        coins = coins - 1
    return pennies

if __name__ == "__main__":
    main()
