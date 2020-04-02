#!/bin/bash

python3 12.py
diff col1.txt <(cut -f 1 ../data/popular-names.txt)
diff col2.txt <(cut -f 2 ../data/popular-names.txt)