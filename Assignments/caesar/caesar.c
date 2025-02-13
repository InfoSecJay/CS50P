#include <cs50.h>
#include <ctype.h> // Needed for isalpha, isupper, and islower
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string s);
char rotate(char letter, int key);

int main(int argc, string argv[])
{
    // Make sure program was run with just one command-line argument
    if (argc != 2) {
        printf("Usage: %s key \n", argv[0]);
        return 1; // Exit with an error code
    }

    // Make sure every character in argv[1] is a digit
    if (!only_digits(argv[1])) {
        printf("Key input is not valid.\n");
        return 1; // Exit with an error code
    }

    // Convert argv[1] from a `string` to an `int`
    int key = atoi(argv[1]);
    printf("The key is: %d\n", key);

    // Prompt user for plaintext
    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");

    // For each character in the plaintext:
    int cipher_length = strlen(plaintext);
    for (int i = 0; i < cipher_length; i++) {
        // Rotate the character if it's a letter, otherwise keep it the same
        char rotated_char = rotate(plaintext[i], key);
        printf("%c", rotated_char);
    }
    printf("\n");

    return 0;
}

// checks if input contains only digits
bool only_digits(string s)
{
    int length = strlen(s);
    for (int i = 0; i < length; i++)
    {
        if (s[i] < '0' || s[i] > '9')  // Check if the character is not a digit
            return false;  // Return false if a non-digit character is found
    }
    return true;  // Return true if all characters are digits
}

char rotate(char letter, int key)
{
    // Check if the character is an uppercase letter
    if (isupper(letter)) {
        return 'A' + (letter - 'A' + key) % 26;
    }
    // Check if the character is a lowercase letter
    else if (islower(letter)) {
        return 'a' + (letter - 'a' + key) % 26;
    }
    // If the character is not a letter, return it as it is
    else {
        return letter;
    }
}
