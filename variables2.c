#include<stdio.h>
int main(){
    int age1, age2;
    int sum;
    printf("Enter age1:");
    scanf("%d", &age1);
    printf("Enter age2:");
    scanf("%d",&age2);
    sum=age1+age2;
    printf("The sum is %d", sum);
    return 0;
}