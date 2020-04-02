with open("col1.txt", "r") as intxt:
    txtl1 = intxt.readlines()
with open("col2.txt", "r") as intxt:
    txtl2 = intxt.readlines()

co = "\n".join([a.strip("\n")+"\t"+b.strip("\n") for a,b in zip(txtl1,txtl2)])

print(co)