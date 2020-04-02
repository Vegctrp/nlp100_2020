with open("../data/popular-names.txt", "r") as intxt:
    txtl = intxt.readlines()

c1 = "\n".join([i.split("\t")[0] for i in txtl])
c2 = "\n".join([i.split("\t")[1] for i in txtl])

with open("col1.txt","w") as out:
    print(c1,file=out)

with open("col2.txt","w") as out:
    print(c2,file=out)