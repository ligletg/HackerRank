#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int array_size;
    cin >> array_size;
    int the_array[array_size];
    for (int j = 0; j < array_size; j++) {
        int tmp = 0;
        cin >> tmp;
        the_array[j] = tmp;
    }


    for (int i = array_size - 1; i >= 0; i--){
        cout << the_array[i];
        if (i > 0) {
            cout << " ";
        }
    }
    cout << endl;
    return 0;
}

