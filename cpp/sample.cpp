// add and multiply
#include <iostream>
/*
using namespace std;
int main(){
    int num1, num2;
    cout << "Enter numners to add and muntiply.\n";
    cin >> num1 >> num2;
    cout << "Sum is " << num1 + num2 << endl;
    cout << "Product is " << num1 * num2 << endl;
    return 0;
}
    */
// positive negative checker
/*
#include <iostream>
using namespace std;
int main (){
    int number;
    cout << "Enter a number to check if its positive, negative or zero\n";
    cin >> number;
    if(number > 0){
        cout << "Positive integer\n";
    } else if(number < 0){
        cout << "Negative integer\n";
    } else {
        cout << "Zero\n";
    }
    return 0;
}
*/
// print numbers from 0 to 20 and their sum
/*
#include <iostream>
using namespace std;
int main (){
    int sum = 0;
    for(int i = 0; i <= 20; i++)
    {
        cout << i << " ";
        sum += i;
    }
    cout << "Sum is " << sum << endl;
    return 0;
}
*/
/*
//largest number in an array
#include <iostream>
using namespace std;
int main(){
    int myArr[5];
    int largest;

    for (int i = 0; i < 5; i++){
        cin >> myArr[i];
    }
    largest = myArr[0];
    for(int i = 1; i < 5; i++){
        if(myArr[i] > largest){
            largest = myArr[i];
        }
    }
    cout << "Largest: " << largest;
    return 0;
}
*/
// functions
/*
#include <iostream>
using namespace std;
int myfunction(int a, int b){
    return a + b;
}
int main(){
    int sum = myfunction(6, 7);
    cout << "sum is: " << sum << endl;
    return 0;
}
*/
/*
//class
#include <iostream>
using namespace std;
class student {
    private:
    string name;
    int marks;
    public:
    void setData();
    void display();
};
void student :: setData()
{
    cin >> name >> marks;
}
void student ::display(){
    cout << "Name: " << name << endl;
    cout << "Marks: " << marks << endl;
}
int main(){
    student s;
    s.setData();
    s.display();
    return 0;
}
*/
/*
//inheritance
#include <iostream>
using namespace std;

class person {
    public:
    string name;
};

class student : public person
{
    public:
    int marks;
    void display();
};

void student :: display(){
    cout << "Name: " << name << endl;
    cout << "Marks: " << marks << endl;
}

int main(){
    student s;
    s.marks = 80;
    s.name = "Fidel";
    s.display();
    return 0;
}
*/
// part two
/*
#include <iostream>
using namespace std;
int main(){
    int n;
    int sum = 0;
    cout << "Enter a number to print numbers between 1 and n\n";
    cin >> n;
    for (int i = 0; i <= n; i++){
        cout << i << " ";
    }
    for (int i = 1; i <= n; i++){
        if(i % 2 == 0){
            sum += i;
        }
    }
    cout << "Sum is: " << sum << endl;
    return 0;
}
*/
/*
#include <iostream>
using namespace std;
int main()
{
    int myArr[5];
    int count = 0;

    for (int i = 0; i < 5; i++)
    {
        cin >> myArr[i];
    }
    for (int i = 0; i < 5; i++)
    {
        if (myArr[i] > 10)
        {
            count++;
        }
    }
    cout << "Count = " << count << endl;
    return 0;
}
*/
/*
//a function that takes 3 numbers and returns the largest
#include <iostream>
using namespace std;
int findMax(int a, int b, int c)
{
    if(a > b && a > c)
    return a;
    else if(b > a && b > c)
    return b;
    else
    return c;
}
int main (){
    cout << "Largest is: " << findMax(5, 890, 67) << endl;

    return 0;
}
    */
/*
//classess
#include <iostream>
using namespace std;

class rectangle {
 private:
 int length;
 int width;

 public:
 void setData();
 int area();
 void display();
};

void rectangle :: setData(){
 cout << "Enter length and width\n";
 cin >> length >> width;
}

int rectangle :: area(){
 return length * width;
}
void rectangle :: display(){
 cout << "The area is: " << area() << endl;
}
int main (){
 rectangle r;
 r.setData();
 r.area();
 r.display();
 return 0;
}
 */

// part 3
//program that accepts number n and prints its factorial
/*
#include <iostream>
using namespace std;
int main (){
    int n;
    int fact = 1;
    cout << "Enter a number to get its factorials\n";
    cin >> n;

    for(int i = 1; i <= n; ++i){
        fact *= i;
    }

    cout << "Factorial of " << n << " are " << fact << endl;
    return 0;
}
*/
/*
//program that stores 6 integers in an array, adds them and gets the average
#include <iostream>
using namespace std;
int main(){
    int array[6];
    int sum = 0;
    float ave = 0;
    cout << "Enter 6 numbers in the array\n";
    for(int i = 0; i < 6; i++){
        cin >> array[i];
    }

    for(int i = 0; i < 6; i++){
        sum += array[i];
    }
    cout << "The sum is " << sum << endl;
    ave = sum / 6;
    cout << "The average is " << ave << endl;
    return 0;
}
*/
/*
//write a function that takes an array with its size and returns numbers that are even in the array
#include <iostream>
using namespace std;
int countEven(int arr[], int size){
    for(int i = 0; i <= size; i++){

    }
}
    */
//classes--a circle
#include <iostream>
using namespace std;

class circle{
    private:
    int radius;

    public:
    void setRadius();
    int calcArea();
    void display();
};
void circle :: setRadius(){
    cout << "Enter the radius\n";
    cin >> radius;
}

int circle :: calcArea(){
    return 3.14 * radius * radius;
}

void circle :: display(){
    cout << "The radius of the circle is: " << calcArea() << endl;
}

int main(){
    circle c;
    c.setRadius();
    c.display();
    return 0;
}