#include <stdio.h>
#include "adds.h"
#include "types.h"
#include "dotproduct.h"

//usage ./app.exe size type
int main(int argc, char **argv)
{
    matrix_t a, b, c;

    // printf("%d\n", argc);
    if (argc != 3)
        return 1;

    int size = atoi(argv[1]);
    int type = atoi(argv[2]);

    init_matrix(a, size, size);
    init_matrix(b, size, size);


unsigned long long beg = 0;
unsigned long long end = 0;

switch(type)
{
     case 1:
        beg = microseconds_now();
        dotproduct_no_tr(a, b, c, size);
        end = microseconds_now();
        break;
    case 2:
        beg = microseconds_now();
        dotproduct_tr(a, b, c, size);
        end = microseconds_now();
        break;
    }

    a[0][0] = 0;
    b[0][0] = 123;
    printf("%llu\n", (end - beg));


    return 0;
}