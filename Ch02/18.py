with open("../data/popular-names.txt", "r") as intxt:
    txtl = intxt.readlines()

nl = list(set([int(lt.split("\t")[2]) for lt in txtl]))
nl.sort(reverse=1)
print("\n".join([str(i) for i in nl]))