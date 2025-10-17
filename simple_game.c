#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    //This generates random number between 0 nad 5
    srand(time(NULL));
    int min = 0;
    int max = 5;
    int random_number = (rand() % (max - min + 1)) + min;
    
    if (random_number == 0)
    {
        printf("Flamingos turn pink from eating shrimp.\n");
    }
    else if (random_number == 1)
    {
        printf("The food that does not spoil is honey.\n");
    }
    else if (random_number == 2)
    {
        printf("Shrimp only swim backwards.\n");
    }
    else if (random_number == 3)
    {
        printf("A taste bus\'s life span is about 10 days.\n");
    }
    else if (random_number == 4)
    {
        printf("It is impossible to sneeze while sleeping.\n");
    }
    else if (random_number == 5)
    {
        printf("It is illigal to sing 0ff-key in North Carolina.\n");
    }
    
    return 0;
}