#ifndef __ADDS_H__
#define __ADDS_H__

#include <time.h>
#include <sys/time.h>
#include "types.h"

unsigned long long microseconds_now(void);

void init(int *array, int size);

void init_matrix(matrix_t matrix, size_t rows, size_t columns);

void print_array(const int *array, int size);

void print_matrix(FILE *file, matrix_t matrix, size_t rows, size_t columns);


#endif
