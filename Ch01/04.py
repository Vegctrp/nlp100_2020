string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
onechar = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dictionary = {}

for i,word in enumerate(string.split(" ")):
    if i+1 in onechar:
        dictionary[word[:1]] = i+1
    else:
        dictionary[word[:2]] = i+1

print(dictionary)