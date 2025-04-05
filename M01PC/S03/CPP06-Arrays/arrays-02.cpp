#include <iostream>
using namespace std;

int main() {
    char vowels[]  = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' };
    // for( char c : vowels ) {
    //  cout << c << endl;
    // }

    int notes[] = { 9, 10, 7, 8, 5, 7, 10, 4 };
    cout << notes[ 3 ] << endl;
    for( int n : notes ) {
        cout << n << endl;
    }





    // cout << vowels[ 0 ] << endl;
    // cout << vowels[ 1 ] << endl;
    // cout << vowels[ 2 ] << endl;
    // cout << vowels[ 3 ] << endl;
    // cout << vowels[ 4 ] << endl;
    // cout << vowels[ 9 ] << endl;

    
    
    return 0;
}
