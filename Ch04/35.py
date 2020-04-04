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
    freq_dic = {}
    for sentence_list in novel_list:
        for word_info in sentence_list:
            if word_info["surface"] in freq_dic:
                freq_dic[word_info["surface"]] += 1
            else:
                freq_dic[word_info["surface"]] = 1
    sorted_freq_dic=sorted(freq_dic.items(), key=lambda e:e[1],reverse=True)
    
    for i in sorted_freq_dic:
        print(i)