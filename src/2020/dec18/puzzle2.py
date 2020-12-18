from src.util import *

lines = parse_string_list_from_file(INPUT)


def paren(line, pos):
    result = ""

    i = pos
    before_plus = 0
    plus_paren = 0
    in_plus = False
    while i < len(line):
        char = line[i]
        if char == " ":
            result += " "
        elif char == "(":
            if not in_plus:
                before_plus = i - pos + plus_paren
            sub_res = paren(line, i + 1)
            plus_paren += sub_res[2]
            result += "(" + sub_res[0]
            i = sub_res[1]
        elif char == ")":
            if in_plus:
                result = result[0:before_plus] + "(" + result[before_plus:i-pos+plus_paren] + ")" + result[i-pos+plus_paren:]
                plus_paren += 2
            return result + ")", i, plus_paren
        elif ord('0') <= ord(char) <= ord('9'):
            if not in_plus:
                before_plus = i - pos + plus_paren
            result += char
        elif char == "+":
            in_plus = True
            result += "+"
        elif char == "*":
            if in_plus:
                result = result[0:before_plus] + "(" + result[before_plus:i-pos+plus_paren-1] + ")" + result[i-pos+plus_paren-1:]
                plus_paren += 2
                in_plus = False
            result += "*"
        else:
            raise ValueError("Unknown character: " + char)
        i += 1

    if in_plus:
        result = result[0:before_plus] + "(" + result[before_plus:] + ")"
    return result, i, plus_paren


paren_lines = [paren(line, 0)[0] for line in lines]
for line in lines:
    print(line, "-->", paren(line, 0)[0])


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


results = [calc(line, 0, "+")[0] for line in paren_lines]

for res in results:
    print(res)
print("")
print(sum(results))
