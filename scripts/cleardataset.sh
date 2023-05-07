#!/bin/bash

for subdir in "../dataset/*"; do
    # echo $subdir
    for typedir in $subdir"/*"; do
        # echo $typedir
        for file in $typedir"/*"; do
            # echo $file
            rm $file
        done
    done
done