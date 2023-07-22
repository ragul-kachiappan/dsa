#include <iostream>
using namespace std;
struct Rectangle {
    int length;
    int breath;
};

struct Complex {
    int real;
    int imaginary;
};

struct Student {
    int roll;
    char name[25];
    char department[25];
    char address[50];
};

struct PlayingCards {
    int face;
    int shape;
    int color;
};

int main() {
    struct Rectangle r;
    struct Rectangle r1 = {10, 5};
    struct PlayingCards deck[52] = {{1,0,0}, {2,0,0}};
    cout << deck[0].face << endl;
    cout << r.length << " " << r.breath;
    cout << endl;
    cout << r1.length << " " << r1.breath;
    cout << endl << "Area = " << r1.length * r1.breath;
    cout << endl;
    return 0;
}