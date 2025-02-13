#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
int coleman_liau(int letters, int words, int sentences);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, sentences
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Calculate the score
    int total = coleman_liau(letters, words, sentences);

    // Print the grade
    if (total < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (total >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", total);
    }

}

int count_letters(string text)
{
    int length = strlen(text);
    int count = 0;
    for (int i = 0 ; i < length; i++)
        if (isalpha(text[i])) count++;  // Count only alphabetic characters
    return count;
}

int count_words(string text)
{
    int length = strlen(text);
    int count = 0;
    for (int i = 0 ; i < length; i++)
        if (text[i] == ' ') count++;
    return count + 1;
}

int count_sentences(string text)
{
    int length = strlen(text);
    int count = 0;
    for (int i = 0 ; i < length; i++)
        if (text[i] == '.' || text[i] == '!' || text[i] == '?') count++;
    return count;
}


int coleman_liau(int letters, int words, int sentences)
{
    // Cast to float to avoid integer division
    float L = 100 * ((float) letters / words);
    float S = 100 * ((float) sentences / words);

    float total = round(0.0588 * L - 0.296 * S - 15.8);
    return total;
}
