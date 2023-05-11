#!/bin/bash

PATHTOTXT="../dataset/processed_data/*"
PATHTOCFG="./gnuplotconfigs/"
PREFIX=$PATHTOCFG"GNUPLOT_"
PATHTOTMPL="./template/"

#clearing other configs
rm $PATHTOCFG*.gpi

#making unique average
for file in $PATHTOTXT; do
    basename=$(basename ${file})
    name=$PREFIX$basename".gpi"
    cat $PATHTOTMPL"base.txt" > $name
    echo "set terminal svg size 1080, 720" >> $name
    echo "set output \"../pictures/${basename}.svg\"" >> $name
    echo "plot \"$file\" using 1:2 with lines title \"$basename\"" >> $name
done

#making unique average with error
for file in $PATHTOTXT; do
    basename=$(basename ${file})
    name=$PREFIX$basename"_Error.gpi"
    cat $PATHTOTMPL"base.txt" > $name
    echo "set terminal svg size 1080, 720" >> $name
    echo "set output \"../pictures/${basename}_Error.svg\"" >> $name
    echo "plot \"$file\" using 1:5:3:7 with yerror title \"$basename Error\", \"$file\" using 1:2 with lines title \"$basename\"" >> $name
done

#making unique average with quatiles (moustache)
for file in $PATHTOTXT; do
    basename=$(basename ${file})
    name=$PREFIX$basename"Moustache.gpi"
    cat $PATHTOTMPL"base.txt" > $name
    echo "set terminal svg size 1080, 720" >> $name
    echo "set output \"../pictures/${basename}Moustache.svg\"" >> $name
    echo "plot \"$file\" using 1:4:3:7:6 with candlesticks title \"$basename Moustache\", \"$file\" using 1:2 with lines title \"$basename\"" >> $name
done

#making comparative graph
name=$PREFIX"Comparative_Graph.gpi"
cat $PATHTOTMPL"base.txt" > $name
echo "set terminal svg size 1080, 720" >> $name
echo "set output \"../pictures/Comparative_Graph.svg\"" >> $name

count=0
for file in $PATHTOTXT; do
    basename=$(basename ${file})
    if [ $count -eq 0 ]; then
        echo "plot \"$file\" using 1:2 with linespoints title \"$basename\", \\" >> $name
    else
        echo "\"$file\" using 1:2 with linespoints title \"$basename\", \\" >> $name
    fi
    count=$((count + 1))
done