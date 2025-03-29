#include <iostream>
using namespace std;

int main() {
    

    int choice = 2;
    switch( choice ) {
        case 2:
            cout << "El valor es: Dos" << endl;
            break;
        case 1:
            cout << "El valor es: Uno" << endl;
            break;
        case 3:
            cout << "El valor es: Tres" << endl;
            break;
        default:
            cout << "El valor es es ditinto a los predeterminados" << endl;
    }
    

    return 0;
}
