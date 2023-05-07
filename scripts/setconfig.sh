#!/bin/bash

cmd="./is_config_valid.sh config.txt"

if [ $# -ne 6 ]; then
    echo "Usage: ./update_data.sh 'options' 'types' 'types of sort' 'count_of_tests' 'sizes_of_tests' 'max_size'"
    exit 1
fi

if [ ! "tiranoslav the rus" = "$1" ]; then
    echo $1 > config.txt
else
    exit 1
fi

if [ ! "tiranoslav the rus" = "$2" ]; then
    echo $2 >> config.txt
else
    exit 1
fi

if [ ! "tiranoslav the rus" = "$3" ]; then
    echo $3 >> config.txt
else
    exit 1
fi

if [ ! "tiranoslav the rus" = "$4" ]; then
    echo $4 >> config.txt
else
    exit 1
fi

if [ ! "tiranoslav the rus" = "$5" ]; then
    echo $5 >> config.txt
else
    exit 1
fi

if [ ! "tiranoslav the rus" = "$5" ]; then
    echo $6 >> config.txt
else
    exit 1
fi

$cmd
echo $?
