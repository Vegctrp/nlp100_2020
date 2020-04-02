with open("../data/popular-names.txt", "r") as intxt:
    txtl = intxt.read()

spt = " ".join(txtl.split("\t"))
print(spt,end="")