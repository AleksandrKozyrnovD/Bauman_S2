#include "dotproduct.h"
#include <stdio.h>

void transpon(matrix_t matrix, size_t size)
{
    for (size_t i = 0; i < size; i++)
    {
        for (size_t j = 0; j < i; j++)
        {
            size_t temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }
}

void dotproduct_no_tr(matrix_t a, matrix_t b, matrix_t c, size_t size)
{
    for (size_t i = 0; i < size; i++)
    {
        for (size_t j = 0; j < size; j++)
        {
            int buf = 0;
            for (size_t k = 0; k < size; k++)
            {
                buf += a[i][k] * b[k][j];
            }
            c[i][j] = buf;
        }
    }
}

void dotproduct_tr(matrix_t a, matrix_t b, matrix_t c, size_t size)
{
    transpon(b, size);
    for (size_t i = 0; i < size; i++)
    {
        for (size_t j = 0; j < size; j++)
        {
            double buf = 0.0;
            for (size_t k = 0; k < size; k++)
            {
                buf += a[i][k] * b[j][k];
            }
            c[i][j] = buf;
        }
    }
    transpon(b, size);
}
