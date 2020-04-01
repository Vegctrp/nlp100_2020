def cipher_operator(char):
    if 97<=ord(char)<123:
        return chr(219-ord(char))
    else:
        return char

def cipher(string):
    return "".join(list(map(lambda char:cipher_operator(char), string)))

print(cipher("123QWERTYqwerty"))

print(cipher(cipher("123QWERTYqwerty")))