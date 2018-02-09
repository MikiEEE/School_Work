//
//  main.h
//  Assignment_2
//
//  Created by MikiEEE on 2/8/18.
//  Copyright © 2018 MiKiEEE. All rights reserved.
//

#ifndef main_h
#define main_h

#include <iostream>
#include <vector>
#include <cstdlib>
#include <stdio.h>
#include <ctime>
#include <random>
using namespace std;

bool findInSet(vector<int> *numbers, int &i, int &index);
void countOccurences(vector<int> *count,const int & index);
void printElements(vector<int> *numbers, vector<int> *count);
void generateSet(vector<int> *set, int &numberOfElements);

#endif /* main_h */
