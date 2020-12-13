input = open("input1", "r")
lines = input.readlines()
partsList = [line.split(" ") for line in lines]

valid = 0
for parts in partsList:
    fromTo = parts[0].split("-")
    fromInt = int(fromTo[0])
    toInt = int(fromTo[1])
    letter = parts[1][0:1]
    password = parts[2]
    # print(fromInt)
    # print(toInt)
    # print(letter)
    # print(password)
    occ = 0
    for character in password:
        if character == letter:
            occ += 1
    if fromInt <= occ and occ <= toInt:
        valid += 1

print(valid)


