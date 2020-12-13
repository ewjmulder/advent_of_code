input = open("input1", "r")
lines = input.readlines()
numbers = [int(line) for line in lines]
print(numbers)

for n1 in numbers:
    for n2 in numbers:
        for n3 in numbers:
            if n1 + n2 + n3 == 2020:
                print(n1 * n2 * n3)
