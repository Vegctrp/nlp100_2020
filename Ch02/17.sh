#!/bin/bash

diff <(python3 17.py) <(cut -f 1 ../data/popular-names.txt | sort | uniq | sort)