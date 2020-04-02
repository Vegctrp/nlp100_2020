with open("./col1.txt", "r") as intxt:
    txtl = intxt.readlines()

print("".join(sorted(list(set(txtl)))), end="")