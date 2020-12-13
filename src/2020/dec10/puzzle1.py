input = open("input1", "r")
lines = input.readlines()
lines = [int(line.rstrip()) for line in lines]

lines.sort()
lines.insert(0, 0)
lines.append(lines[-1] + 3)

print(lines)

ones = 0
trees = 0
for i in range(0, len(lines) - 1):
    if lines[i + 1] - lines[i] == 1:
        ones += 1
    elif lines[i + 1] - lines[i] == 3:
        trees += 1

print(ones * trees)
