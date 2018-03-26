
/*
Reminder: "set" Needs to be sorted
*/
i
#include "main.h"


int main(int argc, const char * argv[]) {
    vector<int> *set = new vector<int>(0);
    vector<int> *numbers = new vector<int>(0);
    vector<int> *count = new vector<int>(0);
    CountOccurences *occur = new CountOccurences();
    bool flag(false);
    int Elements = 10000;
    int index = 0;
    // default set
   // *set =  {1,1,2,2,2,4,5,5,7,7,7};
    generateSet(set, Elements);
    for(unsigned int i = 0; i < set->size(); i++) {
        if(occur->findInSet(numbers, set->at(i), index) || flag) {
            occur->countOccurences(count, index);
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
    occur->printElements(numbers, count);
    
    delete set;
    delete numbers;
    delete count;
    delete occur;
        return 0;
}





void generateSet(vector<int> *set, int &numberOfElements) {
    uniform_int_distribution<int> dice(1,15);
    uniform_int_distribution<int> smallDice(1,9);
    mt19937 random;
    random.seed(time(0));
    
    set->at(0) = dice(random);
    for(unsigned int i = 1; i < numberOfElements; i++) {
        if(set->at(i - 1) == dice(random)) {
            set->at(i) =(dice(random));
        }
        else {
            set->at(i) = dice(random);
        }
    }
    return;
}