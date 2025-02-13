"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed.

Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

"""

def main():

    total_coins = 0
    total_cost = 50

    while 0 <= total_coins < 50:
        print(f"Amount Due: {total_cost}")
        new_coin = int(input("Insert Coin: "))
        match new_coin:
            case 5 | 10 |25:
                total_coins +=  new_coin
                total_cost -= new_coin
            case _:
                print(end="")
    else:
        change_owed = total_coins - 50
        print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()
