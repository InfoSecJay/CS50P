#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
        // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Take average of red, green, and blue
            int rgbt = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);

            // Update pixel values
            image[i][j].rgbtBlue = image[i][j].rgbtGreen = image[i][j].rgbtRed = rgbt;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
             // Compute sepia values
            int sepiaRed  = round((.189 * image[i][j].rgbtBlue + .769 * image[i][j].rgbtGreen + .393 * image[i][j].rgbtRed));
            int sepiaGreen  = round((.168 * image[i][j].rgbtBlue + .686 * image[i][j].rgbtGreen + .349 * image[i][j].rgbtRed));
            int sepiaBlue  = round((.131 * image[i][j].rgbtBlue + .534 * image[i][j].rgbtGreen + .272 * image[i][j].rgbtRed));

            // Update pixel with sepia values
            image[i][j].rgbtRed = (sepiaRed > 255) ? 255 : sepiaRed;
            image[i][j].rgbtGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;
            image[i][j].rgbtBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;

        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixel rows
    for (int i = 0; i < height; i++)
    {
        // For each row, loop up to halfway and swap the pixles
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = temp;

        }
    }
}


// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;

}
