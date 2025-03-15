#include <iostream>
using namespace std;

int main() {
    // Logical Operators
    // and, or, !
    
    // and
    cout << ( 1 == 1 and 2 == 2 and 3 == 2 + 1  ) << endl;
    cout << ( 1 == 1 and 2 == 2 and 3 == 2 + 2  ) << endl;
    cout << ( 1 == 1 and 2 == 3 and 3 == 2 + 2  ) << endl;
    cout << ( 1 == 2 and 2 == 3 and 3 == 2 + 2  ) << endl;

    // or
    cout << ( 1 == 1 or 2 == 2 or 3 == 2 + 1  ) << endl;
    cout << ( 1 == 1 or 2 == 2 or 3 == 2 + 2  ) << endl;
    cout << ( 1 == 1 or 2 == 3 or 3 == 2 + 2  ) << endl;
    cout << ( 1 == 2 or 2 == 3 or 3 == 2 + 2  ) << endl;

    // !
    cout << false << endl;
    cout << true << endl;
    cout << ! false << endl;
    cout << ! true << endl;
    cout << !!! false << endl;
    cout << !!! true << endl;

    return 0;
}
