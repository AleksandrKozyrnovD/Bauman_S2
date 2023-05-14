#include <stdio.h>
#include <stdlib.h>
#include "adds.h"


unsigned long long microseconds_now(void)
{
    struct timeval value;

    if (gettimeofday(&value, NULL))
        return (unsigned long long) -1;
    
    return value.tv_sec * 1000ULL + value.tv_usec / 1000ULL;
}


void init(int *array, int size)
{
    srand(time(NULL));
    for (int i = 0; i < size; i++)
        array[i] = (rand() % (size * 3));
}

void init_sorted(int *array, int size)
{
    for (int i = 0; i < size; i++)
        array[i] = i;
}

void print_array(const int *array, int size)
{
    for (int i = 0; i < size; i++)
        printf("%d ", array[i]);
    printf("\n");
}

void print_array_into_file(FILE *file, int *array, int size)
{
    for (int i = 0; i < size; i++)
    {
        fprintf(file, "%d ", array[i]);
    }
    fprintf(file, "\n");
}