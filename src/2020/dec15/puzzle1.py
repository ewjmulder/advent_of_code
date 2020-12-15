from src.util.parser import *

numbers = parse_number_grid_from_file(INPUT, separator=",")[0]

print(numbers)


def last_index(lst, value):
    lst.reverse()
    i = lst.index(value)
    lst.reverse()
    return len(lst) - i - 1


for i in range(len(numbers) + 1, 2021):
    last = numbers[-1]
    list_until_last = numbers[0:-1]
    if last in list_until_last:
        last_i = last_index(list_until_last, last)
        numbers.append((i - 1) - (last_i + 1))
    else:
        numbers.append(0)

print(numbers)
print(numbers[2019])


