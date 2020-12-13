input = open("input1", "r")
lines = input.readlines()
lines = [line.rstrip() for line in lines]


# Return the Hamming distance between string1 and string2.
# string1 and string2 should be the same length.
def hamming_distance(string1, string2):
    # Start with a distance of zero, and count up
    distance = 0
    # Loop over the indices of the string
    L = len(string1)
    for i in range(L):
        # Add 1 to the distance if these two characters are not equal
        if string1[i] != string2[i]:
            distance += 1
    # Return the final count of differences
    return distance


for line1 in lines:
    for line2 in lines:
        if line1 == line2:
            continue
        if hamming_distance(line1, line2) == 1:
            print(line1)
            print(line2)

