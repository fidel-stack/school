#include <iostream>
using namespace std;
class animal
{
    public:
    void move();
};
class bird : public animal//inheritance
{
    public:
    int wings;
    void move();

};
    void animal::move()
    {
        cout<< "Animal moving\n";
    }
    void bird::move()
    {
        cout<< "Bird flying\n";
    }      
    int main()
    {
        bird a;
        a.move();
        return 0;
    }