//
//  RTOS.hpp
//  main
//
//  Created by Michael Emperador on 4/9/18.
//  Copyright © 2018 Michael Emperador. All rights reserved.
//

#ifndef RTOS_hpp
#define RTOS_hpp

#include "Task.hpp"
#include <unistd.h>

class RTOS : public node {
    typedef void (*FUNCTION)(node*);
    public:
        RTOS(unsigned int TIMEDELAY = 0,unsigned int mode = 0,int prior = 0);
        node* Scheduler();
        void wait();
        void startTask(node* taskCursor);
        void task();
        void startOS();
        void createTask(Task::FUNCTION function, int priority = 0);
        int getReady();
        int getPriority();
        void insertTimerFunction(RTOS::FUNCTION function);
        node* navigate(node*& pointer,char side);
        void print();
        ~RTOS();
    
        node *listHead;

        friend void insertTree ( int key ,Task::FUNCTION funct, node* &current );
        friend void printTree(node *root);
   
protected:
        unsigned int operationMode;
        node *cursor;
        node *taskPointer;
        int base;
        int priority;
        int ready = 1;
        unsigned int delay; // milliseconds
        RTOS::FUNCTION Timer;
        
};
void insertTree ( int key ,Task::FUNCTION funct, node* &current );
void printTree(node *root);

#endif /* RTOS_hpp */
