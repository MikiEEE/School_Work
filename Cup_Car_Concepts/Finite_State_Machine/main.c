//
//  main.c
//  State_Machine
//
//  Created by Michael Emperador on 3/8/18.
//  Copyright © 2018 Michael Emperador. All rights reserved.
//

/*
 just proof ofconcept to give group ideas for means of controlling a cup car that will be run by the kl25z
*/

#include <stdio.h>
#include <stdbool.h>

void (*state)(void);
void start(void);
void go(void);
void turnLeft(void);
void turnRight(void);
void slow(void);
void speed(void);
void stop(void);
void scan(void);
void setup(void);

int save_Distance;
int distance  = 0;

int main(int argc, const char * argv[]) {
    setup();
    return 0;
}

void setup() {
   state = &start;
    int i = 1000;
    for(;i > 0; i--) {
        state();
    }
    return;
}


void start() {
       state = &scan;
        printf("in start \n");
    return;
}

void turnLeft() {
    if(distance < 3) {
        state = &turnRight;
        save_Distance = distance;
    }
    return;
}

void turnRight() {
    if(distance < save_Distance) {
        //Needs state transition
        
    }
}

void go() {
    printf("ROBOT IS GOING \n");
    scanf("%d",&distance );
    if(distance < 3) {
        state = &scan;
    }
    return;
}

void scan() {
    printf("ROBOT IS SCANNING \n");
    scanf("%d",&distance );
    if(distance > 9) {
        state = &go;
    }
    return;
}
