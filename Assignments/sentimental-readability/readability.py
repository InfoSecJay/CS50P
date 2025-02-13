

def main():
    user_input = input("Text: ")

    letters = count_letters(user_input)
    words = count_words(user_input)
    sentences = count_sentences(user_input)

    score = coleman_liau(letters, words, sentences)

    if score < 1:
        print("Before Grade 1")
    elif score >=16:
        print("Grade 16+")
    else:
        print(f"Grade {score}")


def count_letters(text):
    length = len(text)
    count = 0
    for i in range(length):
        if text[i].isalnum():
            count += 1
    return count

def count_words(text):
    length = len(text)
    count = 0
    for i in range(length):
        if text[i] == ' ':
            count += 1
    return count + 1

def count_sentences(text):
    length = len(text)
    count = 0
    for i in range(length):
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            count += 1
    return count


def coleman_liau(letters, words, sentences):
    L = 100*(letters/words)
    S = 100*(sentences/words)

    total = round(0.0588 * L - 0.296 * S - 15.8)
    return total


if __name__ == "__main__":
    main()
