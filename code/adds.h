#ifndef __ADDS_H__
#define __ADDS_H__

#include <time.h>
#include <sys/time.h>

unsigned long long microseconds_now(void);

void init(int *array, int size);

void init_sorted(int *array, int size);

void print_array(const int *array, int size);

void print_array_into_file(FILE *file, int *array, int size);

#endif
