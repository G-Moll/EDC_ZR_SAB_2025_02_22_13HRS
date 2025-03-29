#include <iostream>
using namespace std;

int main() {
    
    for( int i = 0; i < 1000; i ++ ) {
        if( i % 16 != 0 ) {
            continue;
        }
        cout << i << " es multiplo de 16" << endl;
    }

    return 0;
}
