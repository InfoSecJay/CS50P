"""
In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
Assume that the user’s input will indeed be in camel case.
"""

def main():
     camel_case = input("CamelCase: ")
     return snake_case(camel_case)

def snake_case(camel_case):
    snake_case = ""
    for i in range(len(camel_case)):
        if camel_case[i].isupper():
            snake_case = snake_case + "_" + camel_case[i].lower()
        else:
            snake_case += camel_case[i]
    print("snake case: ", snake_case)

main()
