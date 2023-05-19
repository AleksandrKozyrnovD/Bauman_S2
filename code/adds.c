#include <stdio.h>
#include <stdlib.h>
#include "adds.h"



unsigned long long microseconds_now(void)
{
    struct timeval value;

    if (gettimeofday(&value, NULL))
        return (unsigned long long) -1;
    
    return value.tv_sec * 1000ULL * 1000ULL + value.tv_usec;
}


void init(int *array, int size)
{
    srand(time(NULL));
    for (int i = 0; i < size; i++)
        array[i] = (rand() % (size * 3));
}

void init_matrix(matrix_t matrix, size_t rows, size_t columns)
{
    srand(time(NULL));
    for (size_t i = 0; i < rows; i++)
        for (size_t j = 0; j < columns; j++)
        {
            matrix[i][j] = (rand() % (rows * columns * 3));
        }
}

void print_array(const int *array, int size)
{
    for (int i = 0; i < size; i++)
        printf("%d ", array[i]);
    printf("\n");
}

void print_matrix(FILE *file, matrix_t matrix, size_t rows, size_t columns)
{
    for (size_t i = 0; i < rows; i++)
    {
        for (size_t j = 0; j < columns; j++)
        {
            fprintf(file, "%d ", matrix[i][j]);
        }
        printf("\n");
    }
}