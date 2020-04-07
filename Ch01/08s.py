def e(s):return "".join([c,chr(219-ord(c))][96<ord(c)<123]for c in s)
print(e("123QWERTYqwerty"))
print(e(e("123QWERTYqwerty")))