#include <iostream>

using namespace std;

int main()
{
    int n;
    int a[10] = { 0, 1, 2, 3, 4, 5}; // rest will be zero, can work with n length, error will be compiler dependent
    // int b[5] = {2, 4, 5, 6, 7};
    for(int x:a) {
        cout << x << endl;
    }
    cout << endl << sizeof(a);
    cout << endl;
    return 0;
}