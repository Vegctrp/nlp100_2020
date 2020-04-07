def make_ngram(l, n, pad):
    ans = []
    for i in range(len(l)-n+1):
        ans.append(pad.join(l[i:i+n]))
    return ans

def make_word_ngram(string, n):
    return make_ngram(string.split(" "), n, " ")

def make_char_ngram(string, n):
    return make_ngram(string, n, "")


string1 = "paraparaparadise"
string2 = "paragraph"
x = set(make_char_ngram(string1, 2))
y = set(make_char_ngram(string2, 2))

print(x,y)

print(x|y, x&y, x-y, y-x)

print("se" in x, "se" in y)