string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

def rm_symbol(word):
    if word[-1]==',' or word[-1]=='.':
        return word[:-1]
    else:
        return word

print(list(map(lambda word:len(rm_symbol(word)), string.split(" "))))