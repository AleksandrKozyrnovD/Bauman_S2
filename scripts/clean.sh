#!/bin/bash


files="./gnuplotconfigs/*.gpi ../pictures/*.png ../pictures/*.svg ../dataset/processed_data/*.txt"

for file in $files; do
    rm "$file"
done
