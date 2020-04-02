#!/bin/bash

diff <(python3 19.py) <(cut -f 1 ../data/popular-names.txt | sort | uniq -c | sort -r | awk '{ print $2; }')