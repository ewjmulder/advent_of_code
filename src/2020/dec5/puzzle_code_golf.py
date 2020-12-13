import re
l=sorted([int(re.sub("[FL]","0",re.sub("[BR]","1",s)),2) for s in open("i")])
print(l[-1],[a+1 for a,b in zip(l[:-1],l[1:]) if b-a>1][0])