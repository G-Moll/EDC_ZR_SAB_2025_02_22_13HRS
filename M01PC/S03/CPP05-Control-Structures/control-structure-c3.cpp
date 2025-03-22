#include <iostream>
using namespace std;

int main() {
    
    int x = 0;

    do {
        x += 100000;
        cout << x << endl;
    }
    while( /*x < 1000000*/ false );
    
    return 0;
}
