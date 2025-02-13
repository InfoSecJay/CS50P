#include <cs50.h>
#include <stdio.h>


int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);


int main(void)
{

    //initalize variables
    int cents;

    // Prompt the user for change owed, in cents
    do
    {
        cents = get_int("Change: ");
    }
    while (cents < 0);


    // Sum the number of quarters, dimes, nickels, and pennies used
    // Print that sum

    int quarters = calculate_quarters(cents);
    cents = cents - (quarters * 25);

    int dimes = calculate_dimes(cents);
    cents = cents - (dimes * 10);

    int nickles = calculate_nickels(cents);
    cents = cents - (nickles * 5);

    int pennies = calculate_pennies(cents);
    cents = cents - (pennies * 1);

    int sum = quarters + dimes + nickles + pennies;

    printf("%d%s", sum, "\n");
}



int calculate_quarters(int cents)
{
    // Calculate how many quarters you should give customer
    // Subtract the value of those quarters from cents

    int quarters = 0;
    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }
    return quarters;

}


int calculate_dimes(int cents)
{
    // Calculate how many dimes you should give customer
    // Subtract the value of those dimes from remaining cents

    int dimes = 0;
    while (cents >= 10)
    {
        dimes++;
        cents = cents - 10;
    }
    return dimes;
}


int calculate_nickels(int cents)
{
    // Calculate how many nickels you should give customer
    // Subtract the value of those nickels from remaining cents

    int nickels = 0;
    while (cents >= 5)
    {
        nickels++;
        cents = cents - 5;
    }
    return nickels;
}

int calculate_pennies(int cents)
{
    // Calculate how many pennies you should give customer
    // Subtract the value of those pennies from remaining cents

    int pennies = 0;
    while (cents >= 1)
    {
        pennies++;
        cents = cents - 1;
    }
    return pennies;

}

