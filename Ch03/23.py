import gzip
import json
import re

def make():
    with gzip.open("../data/jawiki-country.json.gz", "rt") as reader:
        for line in reader:
            injson=json.loads(line)
            if injson["title"]=="イギリス":
                england_txt = injson["text"]
    return england_txt


if __name__ == '__main__':
    england_txt = make()
    pattern = r"(={2,5})\s?(.+?)\s?\1"
    repatter = re.compile(pattern)

    for line in england_txt.split("\n"):
        match = repatter.findall(line)
        if len(match)>0:
            print(match[0][1], len(match[0][0])-1)