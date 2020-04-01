def e(s):return "".join(96<ord(c)<123and chr(219-ord(c))or c for c in s)
print(e("123QWERTYqwerty"))
print(e(e("123QWERTYqwerty")))