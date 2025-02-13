"""
In a file called adieu.py, implement a program that prompts the user for names,
one per line, until the user inputs control-d. Assume that the user will input
at least one name. Then bid adieu to those names, separating two names with one
and, three names with two commas and one and, and names with commas and one and,
as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
"""

import inflect

p = inflect.engine()
names = []

def main():
    while True:
        try:
            user_input = input("Name: ")
            names.append(user_input)
        except EOFError:
            break

    name_list = p.join(names)
    print("Adieu, adieu, to", name_list)

if __name__ == "__main__":
    main()
