#!/bin/bash

diff <(python3 15.py 2) <(tail -n 2 ../data/popular-names.txt)