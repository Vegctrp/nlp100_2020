def make_ngram(l, n, pad):
    ans = []
    for i in range(len(l)-n+1):
        ans.append(pad.join(l[i:i+n]))
    return ans

def make_word_ngram(string, n):
    return make_ngram(string.split(" "), n, " ")

def make_char_ngram(string, n):
    return make_ngram(string, n, "")

string = "I am an NLPer"

print(make_char_ngram(string, 2))
print(make_word_ngram(string, 2))