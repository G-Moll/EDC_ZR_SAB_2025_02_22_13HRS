#include <iostream>
using namespace std;

int main() {
    
    int x = 0;
    while( x < 1000000 ) {
        x += 1000;
        cout << x << endl;
        if( x >= 15000 ) {
            break;
        }
    }
    
    return 0;
}
