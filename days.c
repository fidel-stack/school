#include <stdio.h>
int main()
{
    int day;
    printf("Enter the day of the week(1-5): \n");
    scanf("%d", &day);

    switch(day)
    {
        case 1:
        printf("Monday!\n");
        break;
        case 2:
        printf("Tusdey!\n");
        break;
        case 3:
        printf("Wednesday!\n");
        break;
        case 4:
        printf("Thursday!\n");
        break;
        case 5:
        printf("Friday!\n");
    }
}