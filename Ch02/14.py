import sys

with open("../data/popular-names.txt", "r") as intxt:
    txtl = intxt.readlines()

n = int(sys.argv[1])
co = "".join(txtl[:n])

print(co,end="")