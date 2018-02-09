/*
Reminder: Output Needs to be sorted
 */

#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <random>
using namespace std;


bool findInSet(vector<int> *numbers, int &i);
void countOccurences(vector<int> *numbers, vector<int> *count,vector<int> *set, const int &i);
void printElements(vector<int> *numbers, vector<int> *count);
void generateSet(vector<int> *set, int &numberOfElements);

int main(int argc, const char * argv[]) {
    vector<int> *set = new vector<int>(0);
    vector<int> *numbers = new vector<int>(0);
    vector<int> *count = new vector<int>(0);
    bool flag(false);
    int Elements = 100;
    // default set
    // *set =  {1,1,2,2,2,4,5,5,7,7,7};
    generateSet(set, Elements);
    for(unsigned int i = 0; i < set->size(); i++) {
        if(findInSet(numbers, set->at(i)) || flag) {
            countOccurences(numbers, count, set, i);
            //cout << numbers->at(numbers->size()-1)<< endl;
            flag = false;
        }
        else {
            numbers->push_back(set->at(i));
            count->push_back(0);
            flag = true;
            i--;
        }
    }
    printElements(numbers, count);
    
    delete set;
    delete numbers;
    delete count;
    
    return 0;
}



void generateSet(vector<int> *set, int &numberOfElements) {
    uniform_int_distribution<int> dice(1,15);
    uniform_int_distribution<int> smallDice(1,9);
    mt19937 random;
    random.seed(time(0));
    
    set->push_back(dice(random) % smallDice(random));
    for(int i = 0; i < numberOfElements - 1; i++) {
        if(set->back() == dice(random) % smallDice(random)) {
            set->push_back(dice(random));
        }
       else if(set->back() < dice(random) % smallDice(random)) {
            set->push_back(set->back());
        }
       else {
           set->push_back(dice(random) % smallDice(random));
       }
    }
    return;
}

void printElements(vector<int> *numbers, vector<int> *count) {
    for(unsigned int d = 0; d < numbers->size(); d++) {
        cout << numbers->at(d) << " : " << count->at(d) << endl;
    }
    return;
}

void countOccurences(vector<int> *numbers, vector<int> *count, vector<int> *set, const int &i) {
    for(unsigned int d = 0; d < numbers->size(); d++) {
        if(numbers->at(d) == set->at(i)) {
            count->at(d)++ ;
        }
    }
    return;
}

bool findInSet(vector<int> *numbers, int &i) {
    for(unsigned int d = 0; d < numbers->size(); d++){
        if(numbers->at(d) == i) {
            return true;
        }
    }
    return false;
}
