from src.util import *

depths = parse_number_list_from_file(INPUT)

print(len(list(filter(lambda tup: tup[1] > tup[0], zip(depths, depths[1:])))))
