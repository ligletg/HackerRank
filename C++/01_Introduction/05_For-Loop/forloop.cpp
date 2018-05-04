#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int start = 0;
    int end = 0;
    string names[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    string defaultValue = "odd";

    cin >> start;
    cin >> end;

    for (int i = start; i <= end; i++) {
        if (i >= 1 && i <= 9) {
            cout << names[i - 1] << endl;
        } else if (i % 2 == 0) {
            cout << "even" << endl;
        } else {
            cout << "odd" << endl;
        }
    }
    return 0;
}

