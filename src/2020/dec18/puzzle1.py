from src.util import *

lines = parse_string_list_from_file(INPUT)


def calc(line, pos, op):
    result = 0
    cur_op = op

    i = pos
    while i < len(line):
        char = line[i]
        if char == " ":
            pass
        elif char == "(":
            sub_res = calc(line, i + 1, "+")
            i = sub_res[1]
            result = eval(f"result {cur_op} {sub_res[0]}")
        elif char == ")":
            return result, i
        elif ord('0') <= ord(char) <= ord('9'):
            result = eval(f"result {cur_op} {int(char)}")
        elif char == "+":
            cur_op = "+"
        elif char == "*":
            cur_op = "*"
        else:
            raise ValueError("Unknown character: " + char)
        i += 1

    return result, i


results = [calc(line, 0, "+")[0] for line in lines]

for res in results:
    print(res)
print("")
print(sum(results))
