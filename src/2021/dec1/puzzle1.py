from src.util import *

depths = Parser.from_file(INPUT).to_number_list()

print(len(list(filter(lambda tup: tup[1] > tup[0], zip(depths, depths[1:])))))
