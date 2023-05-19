#!/bin/bash


files="./gnuplotconfigs/*.gpi ../pictures/* ../dataset/*/*/*.txt ../dataset/processed_data/*"

for file in $files; do
    rm "$file"
done
