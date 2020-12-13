[print(sum([len(f(*l)) for l in [[set(s) for s in g.split("\n")] for g in open("i").read().split("\n\n")]])) for f in [set.union,set.intersection]]
