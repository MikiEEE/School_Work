# Data_Structures_Project
Priority Queue Project
This project is an Implementaion of a Real Time Operating System.  (RTOS)
Its' purpose is to serve as a framework to execute tasks in the order of the tasks' priority.
With a library of functions, RTOS class when used with hashing can take in a string(key asociated with function) and a priority (int). I see many applications with this in (but not limited to) robotics as well as bringing robotics to people who do not know how to code (with documentation of library).

DEMO USAGE:
* This current version of master currently has two function with properly associated timers.
* You can use the functions as much as you like with different priorities.
* Functions with timers are: lungs, Heart (it is not case sensitive).
* When you run you will see it print out the name of the function and the priority. The priority print out is in the Task.task() function and can be removed.  
* If the function does not exist in the hash the command line will say "null function"

Things needed to use RTOS CLASS:
*Library of void functions that take in no parameter (this will be subject to change as development continues).
*A timer function or update function to update the tasks as time passes. (void function that takes in a node pointer as its' parameter)
*The node and task class along with helper functions.hpp/.cpp
*node class
*task class
*hashtableclass
*helperFunctions class (will be moved into RTOS as friends eventually)

Usage of RTOS class (without hashing):
*Instatiate class ex: RTOS foo(0)
*To add tasks to the queue ex: foo.createTask(&functionToAdd,priority)
*To add timer/update(optional) ex: foo.insertTimerFunction(&timerOrUpdateFunction)

Usage of RTOS class (with hashing):
*the hashtabe class takes in function pointer and stores them in an array withan assigned key. When given that key it returns the function pointer. 
*hashtable class has a set capacity of 503 functions this will be subject to change
*hashtable class is instantiated with no parameters hashtable hash;
*hashtable class is populated by hash.popArray("key", &functionto pass)
*At the moment, the hash class is not integrated into the RTOS class so it must be used seperately (foo.createTask(hash.getFunction("userstring",priority)
*Closed and open hashing method is still be decided on. 


Inspirations & acknowledgements:
Idea initailly inspired by Microcomputer Systems Two class guest speaker Bob.
RTOS structure inpired by https://github.com/smartrtos/RTOS.
