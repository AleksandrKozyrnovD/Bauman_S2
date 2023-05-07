#include <stdio.h>
#include <stdlib.h>
#include "sort.h"
#include "adds.h"

#ifndef NMAX
#error NMAX IS NOT DEFINED
#endif

typedef int array_t[NMAX];

int main(int argc, char **argv)
{
    array_t array;

    // printf("%d\n", argc);
    if (argc != 4)
        return 1;

    int type = atoi(argv[1]);
    int size = atoi(argv[2]);
    int type_of_sort = atoi(argv[3]);

    switch (type_of_sort)
    {
        case 1:
            init(array, size);
            break;
        case 2:
            init_sorted(array, size);
            break;
    }

    unsigned long long beg;
    unsigned long long end;
    switch (type)
    {
        case 1:
            beg = microseconds_now();
            insertion_sort1(array, size);
            end = microseconds_now();
            break;
        case 2:
            beg = microseconds_now();
            insertion_sort2(array, size);
            end = microseconds_now();
            break;
        case 3:
            beg = microseconds_now();
            insertion_sort3(array, array + size);
            end = microseconds_now();
            break;
        default:
            return 1;
    }

    printf("%llu\n", (end - beg));
    // FILE *checks = fopen("../code/results/test.txt", "w");
    // print_array_into_file(checks, array, size);
    // fclose(checks);

    return 0;
}