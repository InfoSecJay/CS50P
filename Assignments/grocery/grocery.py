""""
In a file called grocery.py, implement a program that prompts the user for items,
one per line, until the user inputs control-d (which is a common way of ending
one’s input to a program). Then output the user’s grocery list in all uppercase,
sorted alphabetically by item, prefixing each line with the number of times the
user inputted that item. No need to pluralize the items. Treat the user’s input
case-insensitively.
"""

grocery_list = {}

def main():
    while True:
        try:
            item = input().upper()
        except EOFError:
            break

        if item in grocery_list:  # if item is in the grocery list, add 1 to its key value
            grocery_list[item] += 1
        else:                     # if item is not in grocery list, add it to the list
            grocery_list[item] = 1

    for item in sorted(grocery_list.keys()):  # list all the items in grocery list, sorted, and print the value (#) and the key (item)
        print(grocery_list[item], item)

if __name__ == "__main__":
    main()
