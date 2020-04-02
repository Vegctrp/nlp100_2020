#!/bin/bash

wc -l ../data/popular-names.txt | cut -f 1 -d ' '
diff <(wc -l ../data/popular-names.txt | cut -f 1 -d ' ') <(python3 10.py)