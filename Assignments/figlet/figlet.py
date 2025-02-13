"""
FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

    Expects zero or two command-line arguments:
        Zero if the user would like to output text in a random font.
        Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
    Prompts the user for a str of text.
    Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
"""

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

def main():

    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))

    elif len(sys.argv) == 3 and sys.argv[2] in fonts and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        figlet.setFont(font=sys.argv[2])

    else:
        sys.exit(f"Please try again using a valid font: {fonts}")

    user_input = input("Input: ")
    print("Output:\n", figlet.renderText(user_input))


if __name__ == "__main__":
    main()
