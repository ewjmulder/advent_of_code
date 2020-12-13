input = open("input1", "r")
lines = input.readlines()
lines = [int(line.rstrip()) for line in lines]

lines.sort()

start = 0
end = lines[-1] + 3

lines.insert(0, start)
lines.append(end)

print(lines)

counts = {}
def count(num):
    if num == end:
        return 1
    nexts = []
    for n in lines:
        if n > num and n <= num + 3:
            nexts.append(n)
    amount = 0
    for n in nexts:
        if counts.get(n):
            amount += counts.get(n)
        else:
            ns = count(n)
            counts[n] = ns
            amount += ns
    return amount


print(count(0))
