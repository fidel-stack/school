#include <iostream>
using namespace std;
class student//base class
//class defination
{
    public:
    int regNo;
    static int classCount;
    student();//constructor
    static void show();
};
int student :: classCount = 0;
void student::show()
{
    cout << "Hello\n";
}
student :: student()
{
    classCount++;
    regNo = classCount;
}
int main ()
{
    student a, b, c, d, e, f, g, h, p;
    cout << "Reg no : " << f.regNo << endl;
    cout << "Class Count " << student::classCount << endl;
    student::show();
    return 0;
}