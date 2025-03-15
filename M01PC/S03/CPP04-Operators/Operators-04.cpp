#include <iostream>
using namespace std;

int main() {
    // Relational Operators
    // Result: bool (true/false)
    //                 1   0
    // = =, ! =, <, < =, >, > = 
    int x = 10;
    int y = 7;
    
    cout << ( x == y ) << endl;
    cout << ( x != y ) << endl;
    cout << ( x < y ) << endl;
    cout << ( x <= y ) << endl;
    cout << ( x > y ) << endl;
    cout << ( x >= y ) << endl;
    return 0;
}
