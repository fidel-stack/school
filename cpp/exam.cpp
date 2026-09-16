#include <iostream>
using namespace std;
class vehicle{
    private: 
    int classno;
    public:
    void drive();
    void reverse();
};
void vehicle::drive()
{
    cout << "Vehicle driving" << endl;
}
void vehicle::reverse()
{
    cout << "Vehicle reversing" << endl;
}
int main()
{
    vehicle a;
    a.drive();
    a.reverse();
    return 0;
}