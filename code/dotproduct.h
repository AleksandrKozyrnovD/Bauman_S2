#ifndef __VARIANTS_H__
#define __VARIANTS_H__

#include "types.h"

void transpon(matrix_t matrix, size_t size);

void dotproduct_no_tr(matrix_t a, matrix_t b, matrix_t c, size_t size);

void dotproduct_tr(matrix_t a, matrix_t b, matrix_t c, size_t size);

#endif
