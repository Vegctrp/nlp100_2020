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

pattern1 = r"(('{2,5})([^']+?)\2)"
rep1=re.compile(pattern1) # 強調
pattern2 = r"(?<!(?:#REDIRECT\s))(\[\[(?!Category:)(?:[^\|]+?\|)??([^\|]+?)\]\])"
rep2=re.compile(pattern2) # 内部リンク
pattern3 = r"((?:\[\[)?(?:ファイル|File):(.+)\|(((?:\[\[?[^\[\]]+?\]\]?)|[^\[\]])+?)(?:$|\]\]))"
rep3=re.compile(pattern3) # ファイル
pattern4 = r"\[(.+?)\]"
rep4 = re.compile(pattern4) # 外部リンク
pattern5 = r"\{\{lang\|(?:.+?)\|(.+?)\}\}"
rep5 = re.compile(pattern5) # 言語
pattern6 = r"\</?(.+?)/?\>"
rep6 = re.compile(pattern6) # HTMLタグ

def operate(txt):
    txt = rep1.sub(r"\3", txt)
    txt = rep2.sub(r"\2",txt)
    txt = rep3.sub(r"\3",txt)
    txt = rep4.sub(r"\1",txt)
    txt = rep5.sub(r"\1",txt)
    txt = rep6.sub(r"",txt)
    return txt

def make_dict():
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
        dic[match[0][0]] = operate(match[0][1])
    return dic


if __name__ == '__main__':
    dic = make_dict()
    #for i in dic:
        #print(i, dic[i])

    import requests

    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": "File:"+dic["国旗画像"],
        "iiprop":"url"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    PAGES = DATA["query"]["pages"]

    print(PAGES)
    print(PAGES["23473560"]["imageinfo"][0]["url"])