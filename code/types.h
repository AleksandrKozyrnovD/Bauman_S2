#ifndef __TYPES_H__
#define __TYPES_H__

#include <stdlib.h>
#include <stddef.h>

#ifndef NMAX
#error NMAX IS NOT DEFINED
#endif

#if NMAX > 100
#error STACKOVERFLOW
#endif

typedef int matrix_t[NMAX][NMAX];

#endif