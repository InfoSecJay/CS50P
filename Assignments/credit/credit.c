#include <cs50.h>
#include <stdio.h>

// Function prototypes
int calculate_checksum(long cc_number);
void check_vendor(long cc_number);

int main(void)
{
    // Prompt the user for cc number
    long cc_number = get_long("Number: ");

    // Count length of the cc_number
    int length = 0;
    long cc = cc_number;
    while (cc > 0)
    {
        cc = cc / 10;
        length++;
    }

    // Check if length is valid
    if (length != 13 && length != 15 && length != 16)
    {
        printf("INVALID\n");
        return 0;
    }

    // Validate checksum and check vendor
    if (calculate_checksum(cc_number))
    {
        check_vendor(cc_number);
    }
    else
    {
        printf("INVALID\n");
    }
}

// Function to calculate checksum based on Luhn's Algorithm
int calculate_checksum(long cc_number)
{
    int sum1 = 0;
    int sum2 = 0;
    long x = cc_number;
    int total = 0;
    int mod1, mod2, d1, d2;

    do
    {
        // Remove last digit and add to sum1
        mod1 = x % 10;
        x = x / 10;
        sum1 += mod1;

        // Remove second last digit
        mod2 = x % 10;
        x = x / 10;

        // Double second last digit and add digits to sum2
        mod2 *= 2;
        d1 = mod2 % 10;
        d2 = mod2 / 10;
        sum2 += d1 + d2;
    }
    while (x > 0);

    total = sum1 + sum2;

    // Check Luhn Algorithm
    return (total % 10 == 0);
}

// Function to determine the card vendor
void check_vendor(long cc_number)
{
    long start = cc_number;
    while (start >= 100)
    {
        start /= 10;
    }

    // Check starting digits for card type
    if ((start / 10 == 5) && (start % 10 >= 1 && start % 10 <= 5))
    {
        printf("MASTERCARD\n");
    }
    else if ((start / 10 == 3) && (start % 10 == 4 || start % 10 == 7))
    {
        printf("AMEX\n");
    }
    else if (start / 10 == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
