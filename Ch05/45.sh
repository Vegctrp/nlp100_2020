#!/bin/bash

cat 45result.txt | sort | uniq -c | sort -r > 45result-1.txt

cat 45result-1.txt | grep -E "\sする"
cat 45result-1.txt | grep -E "\s見る"
cat 45result-1.txt | grep -E "\s与える"