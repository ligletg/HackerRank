#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int myInt = 0;
    long myLong = 0;
    long long myLlong = 0;
    char myChar = 0;
    float myFloat = 0.0;
    double myDouble = 0.0;
    scanf("%d %ld %lld %c %f %lf", &myInt, &myLong, &myLlong, &myChar, &myFloat, &myDouble);
    printf("%d\n%ld\n%lld\n%c\n%.2f\n%.5lf", myInt, myLong, myLlong, myChar, myFloat, myDouble);
    return 0;
}

