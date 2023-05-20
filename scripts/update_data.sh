#!/bin/bash

# newconfig="./setconfig.sh \"$1\" \"$2\" \"$3\" \"$4\" \"$5\""

# $newconfig
# echo $newconfig

i=0
while read -r line; do
    if [ $i -eq 0 ]; then
        options=$line
    fi
    if [ $i -eq 1 ]; then
        types=$line
    fi
    if [ $i -eq 2 ]; then
        count_of_tests=$line
    fi
    if [ $i -eq 3 ]; then
        size_of_tests="${line}"
    fi
    # if [ $i -eq 5 ]; then
    #     maxsize=$line
    # fi
    i=$((i + 1))
done < config.txt


# echo $options
# echo $types
# echo $types_of_sort
# echo $count_of_tests
# echo $size_of_tests
# echo $maxsize

for option in $options; do
    # echo $option
    for type in $types; do
        # echo $type
        for size in $size_of_tests; do
            j=0
            echo ../dataset/"${type}"/"${option}"/"${size}".txt
            while [ $j -lt "$count_of_tests" ]; do
                # echo ../applications/main"${option}".exe "${type}" "${size}" "${type_of_sort}"
                # Разве это ошибка для shellcheck?
                echo "$(../applications/main"${option}".exe "${size}" "${type}")" >> ../dataset/"${type}"/"${option}"/"${size}".txt
                j=$((j + 1))
            done
        done
    done
done


