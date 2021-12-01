from src.util import *

depths = parse_number_list_from_file(INPUT)

depths_per_3 = list(map(sum, zip(depths, depths[1:], depths[2:])))
print(len(list(filter(lambda tup: tup[1] > tup[0], zip(depths_per_3, depths_per_3[1:])))))
