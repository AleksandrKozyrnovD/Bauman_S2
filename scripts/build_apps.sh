#!/bin/bash

path_to_main="../code/*.c"
path_to_bin="../applications/"
flags="-std=c99 -Wall -Werror -Wextra -Wpedantic -Wvla"

i=0
while read line; do
    if [ $i -eq 0 ]; then
        options=$line
    fi
    if [ $i -eq 1 ]; then
        types=$line
    fi
    if [ $i -eq 2 ]; then
        types_of_sort=$line
    fi
    if [ $i -eq 3 ]; then
        count_of_tests=$line
    fi
    if [ $i -eq 4 ]; then
        size_of_tests="${line}"
    fi
    if [ $i -eq 5 ]; then
        nmax=$line
    fi
    i=$((i + 1))
done < config.txt

for option in $options; do
    cmd="gcc $flags $path_to_main "-$option" -o $path_to_bin""main"${option}".exe"" -DNMAX="${nmax}""
    # echo $cmd
    $cmd
done

