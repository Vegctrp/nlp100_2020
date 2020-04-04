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
    neko_coocfreq_dic = {}
    for sentence_list in novel_list:
        flag=0
        for word_info in sentence_list:
            if word_info["surface"]=="猫":
                flag=1
        if flag:
            for word_info in sentence_list:
                if word_info["surface"] != "猫":
                    if word_info["surface"] in neko_coocfreq_dic:
                        neko_coocfreq_dic[word_info["surface"]] += 1
                    else:
                        neko_coocfreq_dic[word_info["surface"]] = 1
    sorted_freq_dic=sorted(neko_coocfreq_dic.items(), key=lambda e:e[1],reverse=True)
    
    label = []
    left = [i for i in range(10)]
    value = []
    for i in sorted_freq_dic[:10]:
        print(i)
        label.append(i[0])
        value.append(i[1])
    plt.bar(left, value, width=0.8)
    plt.xticks(left, label, fontproperties=fp)
    plt.title("037")
    plt.xlabel("猫との共起頻度が高い10形態素",fontproperties=fp)
    plt.ylabel("出現頻度",fontproperties=fp)
    #plt.show()
    plt.savefig("figure37.png")