//
//  Sort.cpp
//  Assignment_2
//
//  Created by MikiEEE on 2/10/18.
//

#include "Sort.hpp"

void Sort :: bubbleSort(vector<int> *set) {
    int temp(NULL);
    for(int i = 0; i < set->size(); i++) {
        for(unsigned long int j = set->size()-1 ; j > 0; j--) {
            if(set ->at(i) > set->at(j)) {
                temp = set->at(j);
                set->at(j) = set->at(i);
                set->at(i) = temp;
            }
        }
    }
    return;
}

void Sort :: merge(vector<int> *set) {
    int i = 0;
    int j = set->size() / 2;
    int k = set + 1;
    
    return;
}

