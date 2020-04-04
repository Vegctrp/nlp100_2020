import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname='/usr/share/fonts/TakaoPGothic.ttf', size=14)

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
    
    value = []
    for i in sorted_freq_dic:
        value.append(i[1])
    plt.hist(value, bins=100, range=(1,100))
    plt.title("038")
    plt.xlabel("出現頻度",fontproperties=fp)
    plt.ylabel("単語数",fontproperties=fp)
    plt.savefig("figure38.png")

    plt.hist(value, bins=100, range=(1,10000), log=True)
    plt.title("038")
    plt.xlabel("出現頻度",fontproperties=fp)
    plt.ylabel("単語数",fontproperties=fp)
    plt.savefig("figure38-log.png")