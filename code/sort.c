#include "sort.h"

void insert1(int *array, int size, int number)
{
    while (size >= 0 && number < array[size])
    {
        array[size + 1] = array[size];
        size--;
    }
    array[size + 1] = number;
}



void insertion_sort1(int *array, size_t n)
{
    for (size_t i = 1; i < n; i++)
    {
        insert1(array, i - 1, array[i]);
    }
}




void insert2(int *array, int size, int number)
{
    while (size >= 0 && number < array[size])
    {
        *(array + size + 1) = *(array + size);
        size--;
    }
    *(array + size + 1) = number;
}



void insertion_sort2(int *array, size_t n)
{
    for (size_t i = 1; i < n; i++)
    {
        insert1(array, i - 1, *(array + i));
    }
}


void insertion_sort3(int *pbeg, int *pend)
{
    for (int i = 1; i < pend - pbeg; i++)
    {
        int j = i;
        while (j > 0 && *(pbeg + j - 1) > *(pbeg + j))
        {
            int temp = *(pbeg + j);
            *(pbeg + j) = *(pbeg + j - 1);
            *(pbeg + j - 1) = temp;
            j--;
        }
    }
}