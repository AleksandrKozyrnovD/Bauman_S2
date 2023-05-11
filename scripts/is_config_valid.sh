#!/bin/bash

if [ $# -ne 1 ]; then
    echo Usage: ./is_config_valid.sh FILE
    exit 0
fi

i=0
while read -r line; do
    echo "$line"
    i=$((i + 1))
done < "$1"

exit "$i"