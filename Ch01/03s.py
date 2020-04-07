s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print([i[-1]<"/"and len(i[:-1])or len(i) for i in s.split(" ")])