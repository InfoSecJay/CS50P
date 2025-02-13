#define the main function which takes in a string input and prints out new converted phrase
def main():
    phrase = str(input("What's your phrase? "))
    print(convert(phrase))


# define a second function that takes a phrase to be converted and returns replaced smiley/unhappy faces
def convert(phrase_to_convert):
    return phrase_to_convert.replace(":)", "🙂" ).replace(":(", "🙁" )

main()
