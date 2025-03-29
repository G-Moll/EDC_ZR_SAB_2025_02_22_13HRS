#include <iostream>
using namespace std;

int main() {
    

    int choice = 4000;
    switch( choice ) {
        case 2:
        case 4:
        case 6:
            cout << "El valor es del primer grupo" << endl;
            break;
        case -10:
        case -7:
        case -9:
            cout << "El valor es del segundo grupo" << endl;
            break;
        case 200:
        case 300:
        case 400:
            cout << "El valor es del tercer grupo" << endl;
            break;
        default:
            cout << "El valor no esta en algun grupo" << endl;
    }
    

    return 0;
}
