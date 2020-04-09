import random

with open("../data/NewsAggregatorDataset/newsCorpora.csv", "r") as intxt:
    inline = intxt.readlines()

select_publisher = ["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]
datas = []

for line in inline:
    if line != "":
        ll = line.split("\t")
        if ll[3] in select_publisher:
            datas.append((ll[4],ll[1]))

random.shuffle(datas)

print("all data :",len(datas))

with open("train.txt", "w") as out:
    for i in datas[:len(datas)*4//5]:
        print(i[0]+"\t"+i[1], file=out)
print("train data :",len(datas[:len(datas)*4//5]))

with open("valid.txt", "w") as out:
    for i in datas[len(datas)*8//10:len(datas)*9//10]:
        print(i[0]+"\t"+i[1], file=out)
print("valid data :",len(datas[len(datas)*8//10:len(datas)*9//10]))

with open("test.txt", "w") as out:
    for i in datas[len(datas)*9//10:]:
        print(i[0]+"\t"+i[1], file=out)
print("test data :",len(datas[len(datas)*9//10:]))