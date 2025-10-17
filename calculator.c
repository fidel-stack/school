#include <stdio.h>
int main()
{
    int num1, num2, choice;
    float answer;
    printf("#####CALCULATOR#####\n");
    printf("Enter the operation you wanna carry out: (1-4)\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    scanf("%d", &choice);

    if (choice == 1)
    {
        printf("Enter the numbers to add separated by space\n");
        scanf("%d" "%d", &num1, &num2);
        answer = num1 + num2;
        printf("The answer is: %.2f\n", answer); //.2 to get the result in 2 dp
    }
    else if (choice == 2)
    {
        printf("Enter the numbers to subtract separated by space\n");
        scanf("%d" "%d", &num1, &num2);
        answer = num1 - num2;
        printf("The answer is: %.2f\n", answer);
    }
    else if (choice == 3)
    {
        printf("Enter the numbers to multiply separated by space\n");
        scanf("%d" "%d", &num1, &num2);
        answer = num1 * num2;
        printf("The answer is: %.2f\n", answer);
    }
    else if (choice == 4)
    {
        printf("Enter the two numbers to divide separated by space\n");
        scanf("%d" "%d", &num1, &num2);
        if (num2 != 0)
        {
            answer = num1 / num2;
            printf("The answer is: %.2f\n", answer);
        }
        else
        {
            printf("ERROR! Cannot divide a number by zero\n");
        }
    }
    return 0;
}