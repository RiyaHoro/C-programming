// C++ program to map elements from vector to map

#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main()
{
    // Vector of keys and values
    vector<int> keys = { 1, 2, 3, 4 };
    vector<string> values
        = { "one", "two", "three", "four" };

    // Map to store key-value pairs
    map<int, string> myMap;

    // Populating map from vectors
    for (int i = 0; i < keys.size(); i++) {
        myMap[keys[i]] = values[i];
    }

    // Accessing elements in the map and printing them
    cout << "Elements in map:" << endl;
    for (auto it : myMap) {
        cout << it.first << ": " << it.second << endl;
    }

    return 0;
}
