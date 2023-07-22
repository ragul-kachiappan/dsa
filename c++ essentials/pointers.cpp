#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

struct Rectangle {
    int length;
    int breath;
};

int main() {
    // int a = 10;
    // int *p;
    // p = &a;
    // cout << a << endl;
    // cout << *p << endl;
    // cout << "Address stored in p: " << p << endl;

    // int a[5] = {2, 4, 6, 8, 10};
    // int *p;
    // p = a;

    // for(int i = 0; i < 5; i++) {
    //     cout << a[i] << endl;
    //     cout << p[i] << endl;        
    // }
    int *p;

    int *p1;
    char *p2;
    float *p3;
    double *p4;
    struct Rectangle *p5;

    cout << sizeof(p1) << endl;
    cout << sizeof(p2) << endl;
    cout << sizeof(p3) << endl;
    cout << sizeof(p4) << endl;
    cout << sizeof(p5) << endl;

    // p = (int *)malloc(5 * sizeof(int));
    p = new int[5];
    for(int i=0; i<5; i++) {
        cout << p[i] << endl;
    }

    p[0] = 10;
    p[1] = 20;
    p[2] = 30;
    p[3] = 40;
    p[4] = 50;



    for(int i=0; i<5; i++) {
        cout << p[i] << endl;
    } 
    
    delete [] p;
    return 0;
}
