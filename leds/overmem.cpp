#include <unistd.h> // for sleep() 

#include <stdio.h>   
#include <stdlib.h> 
 
int main(void) 
{
    double *p; 
    unsigned long int n = 1024<<16;
    while( p = (double*) malloc(1024*sizeof(double*)) ) 
    {
        n << 2;
        sleep(0.5);
    }

    
    /*double **p = (double**) malloc(800000*sizeof(double*));  // allocates enough for an array of 4 int
 
    for(int n=0; n< 800000; ++n) // populate the array
    {    
        p[n] = (double*) malloc(800000*sizeof(double));
        if (n%1000 == 0)
        {
            sleep(0.01);
            fork();
        }
    }
    for(int n=0; n< 800000; ++n) // populate the array
    {    
        delete[] p[n];
        //sleep(0.0001);
    }
 
    delete[] p;*/
}
