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
    begin=r"{{基礎情報 国"
    end=r"}}"
    info_strings = []
    dic={}

    in_info = 0
    for line in england_txt.split("\n"):
        if line.strip("\n")==end:
            in_info=0
        if in_info:
            if line[0]=="|":
                info_strings.append(line[1:])
            else:
                info_strings[-1] += line
        if line.strip("\n")==begin:
            in_info=1

    pattern=r"(.+)\s=\s(.+)"
    repatter=re.compile(pattern)
    for i in info_strings:
        match=repatter.findall(i)
        dic[match[0][0]] = match[0][1]
    
    print(dic)