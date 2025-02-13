"""
In a file called twttr.py, implement a program that prompts
the user for a str of text and then outputs that same text but
with all vowels (A, E, I, O, and U) omitted, whether inputted in
uppercase or lowercase.
"""

def main():
    user_input = input("Input: ")
    print(f"Output: {shorten(user_input)}")


def shorten(word):
    new_word = ""
    for letter in word:
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            new_word += letter
    return new_word


if __name__ == "__main__":
    main()
