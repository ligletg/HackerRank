#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    int n;
    string names[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "Greater than 9"};
    cin >> n;
    // your code goes here
    if (n <= 9) {
        cout << names[n - 1] << endl;
    } else {
        cout << names[9] << endl;
    }
    return 0;
}
