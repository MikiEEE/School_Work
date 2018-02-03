//
//  main.cpp
//  Assignment_1
//
//  Created by Michael Emperador on 1/23/18.
//  Copyright © 2018 Michael Emperador. All rights reserved.
//

/*
 The purpose of this assignment is to make a triangle of an alternating pattern determined by the
 contents of @symbols array
 */

#include <iostream>

void prompt(int* numRows_ptr);
void spaceMaker(int* division_ptr, int* numRows_ptr);
void forOddNumbers(char* symbol1,char* symbol2,int* d);
void forEvenNumbers(char* symbol1, char* symbol2, int* d);
void setDivision(int* numRows_ptr, int* division_ptr);

using namespace::std;
int main(int argc, const char * argv[]) {
    int numRows;
    int numColumns = 1;
    int d = 0;
    int i = 0;
    int division = 0;
    char symbols[2] = {'^','*'};
    char* symbols_ptr = &symbols[0];
    int* division_ptr = &division;
    int* numRows_ptr = &numRows;
    int* dControl_ptr = &d;
    int* iControl_ptr = &i;
    int* numColumns_ptr = &numColumns;

    prompt(numRows_ptr);
    setDivision(numRows_ptr, division_ptr);
    
    for(; *iControl_ptr < *numRows_ptr; (*iControl_ptr)++) {
            spaceMaker(division_ptr , numRows_ptr);
        for(*dControl_ptr = numColumns -1; *dControl_ptr >= 0; (*dControl_ptr)--) {
            if((*iControl_ptr) % 2 != 1) {
                forOddNumbers(symbols_ptr,(symbols_ptr +1), dControl_ptr);
                }
            else {
                forEvenNumbers((symbols_ptr +1), symbols_ptr,dControl_ptr);
            }
        }
        (*numColumns_ptr)+=2;
        cout << endl;
    }
    return 0;
}

void spaceMaker( int* division_ptr, int* numRows_ptr) {
    for(int i = 0; i < *division_ptr + *numRows_ptr ; i++) {
        cout << ' ';
    }
    (*division_ptr)--;
    return;
}

void forOddNumbers(char* symbol0,char* symbol1,int* dControl_ptr) {
    if(*dControl_ptr % 2 != 0){
        cout << *symbol0;
    }
    else {
        cout << *symbol1;
    }
    return;
}

void forEvenNumbers(char* symbol1, char* symbol0, int* dControl_ptr) {
    if(*dControl_ptr % 2 != 0){
        cout << *symbol1;
    }
    else {
        cout << *symbol0;
    }
    return;
}

void setDivision(int* numRows_ptr, int* division) {
    *division = *numRows_ptr/2;
    return;
}

void prompt(int* numRows_ptr) {
    cout << "Enter the height of your triangle:" << endl;
    cin >> *numRows_ptr;
    return;
    
}

