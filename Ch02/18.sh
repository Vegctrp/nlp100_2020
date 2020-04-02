#!/bin/bash

diff <(python3 18.py) <(cut -f 3 ../data/popular-names.txt | sort | uniq | sort -r -n)