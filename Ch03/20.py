import gzip
import json

with gzip.open("../data/jawiki-country.json.gz", "rt") as reader:
    for line in reader:
        injson=json.loads(line)
        if injson["title"]=="イギリス":
            england_txt = injson["text"]

print(england_txt)