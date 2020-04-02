#!/bin/bash

diff <(python3 14.py 2) <(head -n 2 ../data/popular-names.txt)