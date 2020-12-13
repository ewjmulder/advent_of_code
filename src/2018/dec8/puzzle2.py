input = open("input1", "r")
lines = input.readlines()
ns = [int(p) for p in lines[0].split(" ")]

print(ns)
num = -1
alpha = "ABCDEFGHIJKLMNOP"

def add_node(pos):
    global num
    num += 1
    my_num = num
    nr_childs = ns[pos]
    nr_meta = ns[pos + 1]
    length = 2
    value = 0
    children = {}
    for i in range(0, nr_childs):
        sub_length, sub_value = add_node(pos + length)
        length += sub_length
        children[i + 1] = sub_value
    if nr_childs > 0:
        # print("childs", alpha[my_num], nr_childs)
        for i in range(pos + length, pos + length + nr_meta):
            # print("check", ns[i], children)
            if ns[i] != 0 and ns[i] in children:
                # print("value count", i, ns[i], children[ns[i]])
                value += children[ns[i]]
    else:
        for i in range(pos + length, pos + length + nr_meta):
            value += ns[i]
    length += nr_meta
    print("")
    # print(children)
    # print(alpha[my_num], nr_childs, nr_meta)
    # print(alpha[my_num], length, value)
    return length, value


length, value = add_node(0)
print(value)
