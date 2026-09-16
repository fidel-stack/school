#include <iostream>
using namespace std;
class animal
{
    private:
    int legs, wings;

    public:
    void move();
    void move(int x);
    void move(int x, int y);
    void move(int x, int y, string h);
};
    void animal::move()
    {
        cout<< "Animal moving\n";
    }
    void animal::move(int x)
    {
        cout<< "Animal walking\n";
    }
    void animal::move(int x, int y)
    {
        cout<< "Animal flying:)\n";
    }    
    int main()
    {
        animal a;
        a.move();
        a.move(4);
        a.move(4, 2);
        return 0;
    }