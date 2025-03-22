#include <iostream>
using namespace std;

int main() {
    /*
	Tenemos actividades para niños, donde las edades serán a partir de los 7 años, hasta los 12.
	1) Taller de dibujo: Edades de 7 a 10
	2) Taller de computo: Edades de 11 a 12
    */

	int age = 7;

	if( age >= 7 and age <= 10 ) {
		cout << "Puedes tomar el taller de Dibujo" << endl;
	}
	else if( age > 10 and age < 13 ) {
		cout << "Puedes tomar el taller de Computo" << endl;
	}
	else {
		cout << "Tu edad no coincide para que tomes las actividades" << endl;
	}

    return 0;
}
