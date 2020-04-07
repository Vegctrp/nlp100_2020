def make_novellist():
    with open("../data/neko.txt.mecab") as intxt:
        alltxt = intxt.read()
        novel_list = []
        for sentence in alltxt.split("EOS"):
            if sentence != "\n":
                sentence_list = []
                for word in sentence.split("\n"):
                    if word != "":
                        winfo = {}
                        winfo["surface"] = word.split("\t")[0]
                        winfo["base"] = word.split("\t")[1].split(",")[6]
                        winfo["pos"] = word.split("\t")[1].split(",")[0]
                        winfo["pos1"] = word.split("\t")[1].split(",")[1]
                        sentence_list.append(winfo)
                novel_list.append(sentence_list)
    return novel_list

if __name__ == '__main__':
    novel_list = make_novellist()
    no_concats = []
    for sentence_list in novel_list:
        for i in range(len(sentence_list)-2):
            if sentence_list[i]["pos"]=="名詞" and sentence_list[i+1]["surface"]=="の" and sentence_list[i+2]["pos"]=="名詞":
                no_concats.append(sentence_list[i]["surface"]+sentence_list[i+1]["surface"]+sentence_list[i+2]["surface"])
    print(no_concats)