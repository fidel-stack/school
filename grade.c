#include<stdio.h>
 int main()
{
    //declaring the variable
int marks;
printf("Enter your marks below: ");
scanf("%d", &marks);
if(marks >= 70)
{
    //if the condition is true then print the following:
    printf("Grade A");
}
else if(marks >= 60 && marks <= 60)
{
    printf("Grade B");
}
else if(marks >= 50 && marks <= 59)
{
    printf("Grade C");
}
else if(marks >= 40 && marks <= 49)
{
    printf("Grade D");
}
else
{
    printf("Fail");
}
    return 0;
}