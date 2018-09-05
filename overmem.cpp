#include <unistd.h> // for sleep() 

#include <stdio.h>   
#include <stdlib.h> 
 
int main(void) 
{
    int **p = (int**) malloc(100000*sizeof(int*));  // allocates enough for an array of 4 int
 
    for(int n=0; n< 100000; ++n) // populate the array
    {    
        p[n] = (int*) malloc(400000*sizeof(int));
        //sleep(0.1);
    }
    for(int n=0; n< 100000; ++n) // populate the array
    {    
        delete[] p[n];
        sleep(0.01);
    }
 
    delete[] p;
}
