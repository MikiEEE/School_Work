//
//  CountOccurences.hpp
//  Assignment_2
//
//  Created by MikIEEE on 2/9/18.
//  Copyright © 2018 MikIEEE. All rights reserved.
//

#ifndef CountOccurences_hpp
#define CountOccurences_hpp
#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
class CountOccurences {
    public:
        bool findInSet(vector<int> *numbers, int &i, int &index);
        void countOccurences(vector<int> *count,const int & index);
        void printElements(vector<int> *numbers, vector<int> *count);
    private:
    
};

#endif /* countOccurences_hpp */

