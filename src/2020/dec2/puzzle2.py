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
    print(fromInt)
    print(toInt)
    print(letter)
    print(password)
    print(password[fromInt - 1])
    print(password[toInt - 1])
    pos_1_ok = password[fromInt - 1] == letter
    pos_2_ok = password[toInt - 1] == letter
    print(pos_1_ok)
    print(pos_2_ok)
    if (pos_1_ok or pos_2_ok) and not (pos_1_ok and pos_2_ok):
        valid += 1
        print("valid")
    else:
        print("invalid")

print(valid)


