s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
r=lambda w:[w,w[:-1]][w[-1]<"/"]
print([len(r(i)) for i in s.split(" ")])