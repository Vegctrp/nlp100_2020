import sys

with open("../data/popular-names.txt", "r") as intxt:
    txtl = intxt.readlines()

n = int(sys.argv[1])
cll = [txtl[i:min(i+n, len(txtl))] for i in range(0,len(txtl),n)]
for i,cl in enumerate(cll):
    with open("./out16/rp-0"+str(i), "w") as out:
        print("".join(cl), file=out, end="")