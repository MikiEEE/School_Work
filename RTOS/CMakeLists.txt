cmake_minimum_required(VERSION 3.10)
project(Data_Structures_Project)

set(CMAKE_CXX_STANDARD 11)

include_directories(main)
include_directories(main/UtilityClasses)
include_directories(main/UtilityClasses/nodeClass)
include_directories(main/UtilityClasses/TaskClass)
include_directories(main/UtilityClasses/hashClass)
include_directories(main/UtilityClasses/RTOSClass)

add_executable(Data_Structures_Project
        main/UtilityClasses/nodeClass/node.cpp
        main/UtilityClasses/nodeClass/node.hpp
        main/UtilityClasses/TaskClass/Task.cpp
        main/UtilityClasses/TaskClass/Task.hpp
        main/UtilityClasses/hashClass/hashtable.h
        main/UtilityClasses/hashClass/hashtable.cpp
        main/TimersandUpdates.hpp
        main/TimersandUpdates.cpp
        main/UtilityClasses/RTOSClass/helperFunctions.cpp
        main/voidFuctionLibrary.hpp
        main/voidFuctionLibrary.cpp
        main/main.cpp
        main/main.h
        main/UtilityClasses/RTOSClass/RTOS.cpp
        main/UtilityClasses/RTOSClass/RTOS.hpp)