import random
string = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

ansl = []

for word in string.split(" "):
    if len(word)<=4:
        ansl.append(word)
    else:
        wl = list(word)[1:-1]
        random.shuffle(wl)
        ansl.append(word[0]+"".join(wl)+word[-1])

print(" ".join(ansl))