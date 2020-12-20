from src.util import *
import re

[rule_lines, messages] = open(INPUT).read().split("\n\n")
rule_lines = parse_string_list_from_string(rule_lines)
messages = parse_string_list_from_string(messages)

rules = {}
characters = {}

for rule_line in rule_lines:
    # print(f"checking line {rule_line}")
    [r, rule_part] = rule_line.strip().split(":")
    if int(r) == 8:
        rule_part = "42 | 42 8"
    elif int(r) == 11:
        rule_part = "42 31 | 42 11 31"
    if rule_part.strip().startswith("\""):
        characters[int(r)] = rule_part[2]
    else:
        rules_or = rule_part.split("|")
        numbers_or = [[int(n) for n in rule_or.strip().split(" ")] for rule_or in rules_or]
        rules[int(r)] = numbers_or

print(rules)
print(characters)

rule_patterns = {}

def calc_rule_pattern(rule_number, depth):
    if depth == 20:
        return ""
    rule_pattern = ""
    if rules.get(rule_number):
        rule = rules[rule_number]
        for i in range(0, len(rule)):
            rs_or = rule[i]
            for r_or in rs_or:
                rule_pattern += calc_rule_pattern(r_or, depth + 1)
            if i < len(rule) - 1:
                rule_pattern += "|"
        rule_pattern = "(" + rule_pattern + ")"
        rule_patterns[rule_number] = rule_pattern
    else:
        rule_pattern = characters[rule_number]
    return rule_pattern


calc_rule_pattern(0, 0)

print(rule_patterns)
print(rule_patterns[0])
pattern = re.compile(rule_patterns[0])
print(pattern)


amount = 0
for message in messages:
    if re.fullmatch(pattern, message):
        print(f"Fully matched {message}")
        amount += 1
    else:
        print(f"No full match for {message}")

print(amount)


