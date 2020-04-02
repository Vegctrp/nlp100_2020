with open("./col1.txt", "r") as intxt:
    txtl = intxt.readlines()

dic = {}

for w in txtl:
    word = w.strip("\n")
    if word in dic:
        dic[word] = dic[word] + 1
    else:
        dic[word] = 1

dic_sorted = sorted(dic.items(), key=lambda x:(x[1],x[0]), reverse=1)
print("\n".join([i[0] for i in dic_sorted]))