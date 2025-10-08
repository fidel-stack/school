#include <stdio.h>

int main() 
{
  int weight, planet;
  printf("Enter your weight below: \n");
  scanf("%d", &weight);
  printf("Enter the number of the planet you want to fight on: \n");
  printf("1. Mercury\n");
  printf("2. Venus\n");
  printf("3. Mars\n");
  printf("4. Jupiter\n");
  printf("5. Saturn\n");
  printf("6. Uranus\n");
  printf("7. Neptune\n");
  scanf("%d", &planet);
  if(planet == 1){
    weight = weight * 0.38;
  }
  else if(planet == 2){
    weight = weight * 0.91;
  }
  else if(planet == 3){
    weight = weight * 0.38;
  }
  else if(planet == 4){
    weight = weight * 2.34;
  }
  else if(planet == 5){
    weight = weight * 1.06;
  }
  else if(planet == 6){
    weight = weight *0.92;
  }
  else if(planet == 7){
    weight = weight * 1.19;
  }
  
  printf("Your weight is: %d\n", weight);


return 0;

}