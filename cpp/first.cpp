#include <fstream>
using namespace std;
int main()
{
    fstream myfile("/home/lambdalord/bsc/");
    
    myfile << "Hello world!";
    return 0;
}