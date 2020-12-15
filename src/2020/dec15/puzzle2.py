from src.util.parser import *

numbers = parse_number_grid_from_file(INPUT, separator=",")[0]

print(numbers)

last_seen = {}
for i in range(0, len(numbers) - 1):
    last_seen[numbers[i]] = i + 1
prev = numbers[-1]

index_to_report = 30000000
# index_to_report = 2020

for i in range(len(numbers) + 1, index_to_report + 1):
    if i % int(index_to_report / 10) == 0:
        print(i / index_to_report * 100, "%")
    last = numbers[-1]
    next = 0
    if last in last_seen:
        last_i = last_seen[last]
        next = (i - 1) - last_i
    numbers.append(next)
    last_seen[prev] = i - 1
    prev = next

# print(numbers)
print(numbers[index_to_report - 1])


