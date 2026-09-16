#include <iostream>
    using namespace std;
    class animal
    {
        public:
        int legs, wings;
        string name;
        void move();
        animal ();//constructor declaration(default)
        animal (int g, int w);//(paramatised)
        animal (animal& orig);//copy constructor
        ~animal ();//destructor
    };
    
    void animal::move()
    {
        cout << "Animal moving...\n";
    }
    animal::~animal()
    {
        cout << "Killing..." << name  <<endl;//destructor
    }
    animal::animal()
    {
        cout << "DC: Creating animal...\n";//constructor(default)
        legs = 2;
        wings = 0;
        name = "A";
    }
    animal::animal(int g, int w)
    {
        cout << "PC: Creating animal...\n";//constructor(paramatised)
        legs = g;
        wings = w;
        name = "C";
    }

    animal::animal(animal& orig)
    {
        cout << "PC: Claoning an animal...\n";//constructor(paramatised)
        legs = orig.legs + 1;
        wings = orig.wings * 2;
        name = "B";
    }

    int main(){
        animal a;
        animal b(4,2);
        a.move();
        animal c (b);

        return 0;
    }