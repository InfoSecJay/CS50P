"""
In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
Assume that the user’s input will indeed be in camel case.
"""

def main():
    camel_case = input("CamelCase: ")
    return snake_case(camel_case)

def snake_case(camel_case):
    
    # print string output "snake_case: "
    print("snake_case: ", end="")
        
    # for the next string results, loop through every letter
    for letter in camel_case:
        
        # check if the letter is an upper
        if letter.isupper():
            
            #if its upper, print an underscore and change the letter to lower and end with white space and not new line
            print("_" + letter.lower(), end="")
        else:
            # if lower, print the letter and do not skip line
            print(letter, end="")
