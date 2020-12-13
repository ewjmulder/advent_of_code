input = open("input1", "r")
lines = input.readlines()
ns = [int(p) for p in lines[0].split(" ")]

print(ns)

tree = {}
metas = 0

def add_node(pos):
    global metas
    nr_childs = ns[pos]
    nr_meta = ns[pos + 1]
    # print(pos, nr_childs, nr_meta)
    length = 2
    for i in range(0, nr_childs):
        length += add_node(pos + length)
    for i in range(pos + length, pos + length + nr_meta):
        metas += ns[i]
        # print(ns[i], metas)
    length += nr_meta
    return length


add_node(0)
print(metas)
