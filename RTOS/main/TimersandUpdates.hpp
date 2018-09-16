//
//  TimersandUpdates.hpp
//  main
//
//  Created by Michael Emperador on 4/20/18.
//  Copyright © 2018 Michael Emperador. All rights reserved.
//
//

#ifndef TimersandUpdates_hpp
#define TimersandUpdates_hpp
#include <ctime>
#include "RTOS.hpp"



double getStartTime();
void zeroOut();
void timeFunction(node* head_ptr);
void traverse(node* &root);
void adjustTime(time_t &hearttime);
void timeInit();
#endif /* TimersandUpdates_hpp */


