#include <iostream>
using namespace std;

int main() {
    
    for( int i = 0; i < 10000; i += 7 ) {
        cout << i << endl;
        if( i >= 50 ) {
            break;
        }
    }

    return 0;
}
