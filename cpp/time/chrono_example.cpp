/*
 * Build: g++ -std=c++11 chrono_example.cpp
 * Reference: http://stackoverflow.com/questions/12937963/get-local-time-in-nanoseconds
 *
 * */

#include <iostream>
#include <chrono>
#include <unistd.h>

using namespace std;

int main()
{
    auto start = std::chrono::high_resolution_clock::now();
    int a=0;
    /*for (int i=0; i<0xff; i++)
    {
        a++;
    }*/
    sleep(1);
            
    auto finish = std::chrono::high_resolution_clock::now();
    std::cout << (long int)std::chrono::duration_cast<std::chrono::nanoseconds>(finish-start).count() << "ns\n";

    return 0;
}



