"""
In a file called twttr.py, implement a program that prompts
the user for a str of text and then outputs that same text but
with all vowels (A, E, I, O, and U) omitted, whether inputted in
uppercase or lowercase.
"""

def main():
    user_input = input("Input: ")
    print("Output: ", end="")

    for letter in user_input:
        if letter.lower() in ["a", "e", "i", "o", "u"]:
            print("", end="")
        else:
            print(letter, end="")

if __name__ == "__main__":
    main()
