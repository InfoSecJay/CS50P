#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char *argv[])
{
    // Your program should accept exactly one command-line argument, the name of a forensic image from which to recover JPEGs.
    // If your program is not executed with exactly one command-line argument, it should remind the user of correct usage, and main should return 1.
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");

    // If the forensic image cannot be opened for reading, your program should inform the user as much, and main should return 1.
    if (card == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Create a buffer for a block of data
    uint8_t buffer[512];

    // Variables to track the JPEG files
    FILE *img = NULL;
    char filename[8];
    int file_count = 0;
    bool found_jpeg = false;

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Check the sequence of four bytes matching jpg or not
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If already found JPEG, close previous file
            if (found_jpeg)
            {
                fclose(img);
            }
            else
            {
                // Mark that its the start of a JPEG
                found_jpeg = true;
            }

            // Create a new JPEG file
            sprintf(filename, "%03i.jpg", file_count);
            img = fopen(filename, "w");
            if (img == NULL)
            {
                printf("Could not create output file.\n");
                fclose(card);
                return 1;
            }

            // Increment the JPEG file count
            file_count++;
        }

        // If currently processing a JPEG, write the buffer to the file
        if (found_jpeg)
        {
            fwrite(buffer, 1, 512, img);
        }
    }

    // Close any remaining open files
    if (img != NULL)
    {
        fclose(img);
    }

    fclose(card);
    return 0;
}
