#include <iostream>
#include <string>
using namespace std;

struct Student {
    int age;
    string name;
    bool registered;
    string topics[ 2 ];
};

Student createStudent( string n, int a, bool r, string m1, string m2 ) {
    Student tempStudent;
    tempStudent.name = n;
    tempStudent.age = a;
    tempStudent.registered = r;
    tempStudent.topics[ 0 ] = m1;
    tempStudent.topics[ 1 ] = m2;
    return tempStudent;
}

int main() {
    Student studentOne = createStudent( "Joshua", 15, true, "Math", "Eng" );
    Student studentTwo = createStudent( "John", 12, false, "Esp", "Dra" );
    Student studentBis = createStudent( "Paul", 17, true, "Spo", "Math" );
    Student students[] = { studentOne, studentTwo, studentBis };
    // Student studentTwo;
    // studentTwo.name = "John";
    // studentTwo.age = 12;
    // studentTwo.registered = false;
    // studentTwo.topics[ 0 ] = "Esp";
    // studentTwo.topics[ 1 ] = "Dra";

    cout << studentBis.age << endl;
    cout << studentBis.name << endl;
    cout << studentBis.registered << endl;
    cout << studentBis.topics[ 0 ] << endl;
    cout << studentBis.topics[ 1 ] << endl;
    return 0;
}
