#include <stdio.h>
int main(int argc, char** argv)
{
	int choice = 0;
	
	while (choice != 3)
	{
        printf("\nMenu:\n");
        printf("1. Say Hello\n");
        printf("2. Add Two Numbers\n");
        printf("3. Exit\n");
        printf("Enter your choice: \n");
        scanf("%d", &choice);
        
        if (choice == 1)
		{
			printf("Hello\n");
		}
		else if (choice == 2)
		{
			int num1, num2;
			printf("Enter the Two numbers to add\n");
			scanf("%d %d", &num1, &num2);
			printf("The sum is %d", num1 + num2);
		}
		else if (choice == 3)
		{
			printf("Exiting program...Bye\n");
		}
		else
		{
			printf("Invalid choice\n");
		}
	}

	
	return 0;
}