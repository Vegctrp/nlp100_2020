#!/bin/bash

diff <(python3 13.py) <(paste -d '\t' col1.txt col2.txt)