input = open("input1", "r")
lines = input.readlines()

i = 0
amounts = []
while i < len(lines):
    letters = None
    while i < len(lines) and lines[i].rstrip() != "":
        line = lines[i].rstrip()
        print(line)
        person_letters = set()
        for char in line:
            person_letters.add(char)
        if letters is None:
            letters = person_letters
        letters = letters.intersection(person_letters)
        i += 1
    amounts.append(len(letters))
    if i < len(lines) and lines[i].rstrip() == "":
        i += 1

print("sum:", sum(amounts))
