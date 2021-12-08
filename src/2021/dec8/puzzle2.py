from src.util import *

lines = Parser.from_file(INPUT).to_lines()

in_outlines = [line.split("|") for line in lines]

# print(in_outlines)

inwords_list = [line.strip().split(" ") for line in [words[0] for words in in_outlines]]
outwords_list = [line.strip().split(" ") for line in [words[1] for words in in_outlines]]

# print(inwords_list)
# print(outwords_list)

numbers = []
for i in range(len(in_outlines)):
    inwords = inwords_list[i]
    outwords = outwords_list[i]

    seg_2 = [set([char for char in word]) for word in inwords if len(word) == 2]
    seg_3 = [set([char for char in word]) for word in inwords if len(word) == 3]
    seg_4 = [set([char for char in word]) for word in inwords if len(word) == 4]
    seg_5 = [set([char for char in word]) for word in inwords if len(word) == 5]
    seg_6 = [set([char for char in word]) for word in inwords if len(word) == 6]
    seg_7 = [set([char for char in word]) for word in inwords if len(word) == 7]

    # print(seg_2[0], seg_6[0], seg_6[1])
    # seg_f = set.intersection(seg_2[0], seg_6[0], seg_6[1])
    # print(seg_f)
    seg_a = set.difference(seg_3[0], seg_2[0]).__iter__().__next__()
    seg_d = set.intersection(seg_5[0], seg_5[1], seg_5[2], seg_4[0]).__iter__().__next__()
    seg_b = set.difference(seg_4[0], set.union(seg_2[0], set(seg_d))).__iter__().__next__()
    count_cf = flatten(seg_6).count([s for s in seg_2[0]][0])
    count_cf2 = flatten(seg_6).count([s for s in seg_2[0]][1])
    if count_cf == 2:
        seg_c = [s for s in seg_2[0]][0]
        seg_f = [s for s in seg_2[0]][1]
    else:
        seg_f = [s for s in seg_2[0]][0]
        seg_c = [s for s in seg_2[0]][1]
    left = seg_7[0] - {seg_a, seg_b, seg_c, seg_d, seg_f}
    count_eg = flatten(seg_6).count([l for l in left][0])
    count_eg2 = flatten(seg_6).count([l for l in left][1])
    if count_eg == 2:
        seg_e = [l for l in left][0]
        seg_g = [l for l in left][1]
    else:
        seg_g = [l for l in left][0]
        seg_e = [l for l in left][1]

    print(seg_a, seg_b, seg_c, seg_d, seg_e, seg_f, seg_g)

    num_str = ""
    for out in outwords:
        if set([o for o in out]) == {seg_c, seg_f}:
            num_str += "1"
        elif set([o for o in out]) == {seg_a, seg_c, seg_f}:
            num_str += "7"
        elif set([o for o in out]) == {seg_a, seg_b, seg_c, seg_e, seg_f, seg_g}:
            num_str += "0"
        elif set([o for o in out]) == {seg_a, seg_c, seg_d, seg_e, seg_g}:
            num_str += "2"
        elif set([o for o in out]) == {seg_a, seg_c, seg_d, seg_f, seg_g}:
            num_str += "3"
        elif set([o for o in out]) == {seg_b, seg_c, seg_d, seg_f}:
            num_str += "4"
        elif set([o for o in out]) == {seg_a, seg_b, seg_d, seg_f, seg_g}:
            num_str += "5"
        elif set([o for o in out]) == {seg_a, seg_b, seg_d, seg_e, seg_f, seg_g}:
            num_str += "6"
        elif set([o for o in out]) == {seg_a, seg_b, seg_c, seg_d, seg_e, seg_f, seg_g}:
            num_str += "8"
        elif set([o for o in out]) == {seg_a, seg_b, seg_c, seg_d, seg_f, seg_g}:
            num_str += "9"

    num = int(num_str)
    print(num)
    numbers.append(num)

print(sum(numbers))
