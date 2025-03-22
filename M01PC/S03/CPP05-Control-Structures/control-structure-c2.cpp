#include <iostream>
using namespace std;

int main() {
    
    int x = 0;
    while( x < 1000000 ) {
        x += 100000;
        cout << x << endl;
    }
    
    return 0;
}
