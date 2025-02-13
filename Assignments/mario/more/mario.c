#include <cs50.h>
#include <stdio.h>

void print_row(int height);

int main(void)
{
    int n;
    do
    {
        n = get_int("Pyramid Height?: ");
    }
    while (n < 1);

    print_row(n);
}

void print_row(int height)
{

    // print n many rows
    for (int i = 0; i < height; i++)
    {

        // print n-1 spaces
        for (int j = 0; j < (height - i - 1); j++)
        {
            printf(" ");
        }

        // print n-(n-1) hashes
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }

        // print 2 spaces
        printf("  ");

        // print n-(n-i) hashes
        for (int k = 0; k <= i; k++)
        {
            printf("#");
        }

        // skip line
        printf("\n");
    }
}
