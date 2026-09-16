#include <iostream>
using namespace std;
class person//base class
//class defination
{
    public:
    int idno;
    virtual void speak();
    void move();
};
class student : public person
{
    public:
    void speak ();
};
void person::move()
{
    cout << "Person moving\n";
}
void person::speak()
{
    cout << "Person speaking:)\n";
}
void student::speak()
{
    cout << "Comrade speaking:)\n";
}
int main(){
    student p;
    //p.speak();
    person * s = &p;
    s -> move();
    s -> speak();
    p.speak();
    return 0;
    cout << p.idno;
}