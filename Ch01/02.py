string1 = "パトカー"
string2 = "タクシー"

print("".join([a+b for a,b in zip(string1, string2)]))