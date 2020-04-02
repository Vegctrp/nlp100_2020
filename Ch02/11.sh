#!/bin/bash

diff <(python3 11.py) <(sed -e 's/\t/ /g' ../data/popular-names.txt)

diff <(python3 11.py) <(cat ../data/popular-names.txt | tr "\t" " ")

diff <(python3 11.py) <(expand -t 1 ../data/popular-names.txt)