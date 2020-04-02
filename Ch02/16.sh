#!/bin/bash

read n

row=`wc -l ../data/popular-names.txt | cut -f 1 -d " "`
echo $row
num=`expr $(($row-1)) / $n + 1`
echo $num

if [ $num -gt 10 ] ; then
    echo "error"
else
    python3 16.py $n
    split -d -l $n ../data/popular-names.txt ./out16/r1-
    for ((i=0;i<$num;i++)); do
        diff "./out16/r1-0${i}" "./out16/rp-0${i}"
    done
fi