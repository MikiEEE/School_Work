#include "CountOccurences.hpp"

void CountOccurences ::printElements(vector<int> *numbers, vector<int> *count) {
    for(int d = 0; d < numbers->size(); d++) {
        cout << numbers->at(d) << " : " << count->at(d) << endl;
    }
    return;
}

void CountOccurences :: countOccurences(vector<int> *count, const int &index) {
    count->at(index)++ ;
    return;
}

bool CountOccurences :: findInSet(vector<int> *numbers, int &i, int &index) {
    for(unsigned int d = 0; d < numbers->size(); d++){
        if(numbers->at(d) == i) {
            index = d;
            return true;
        }
    }
    return false;
}

